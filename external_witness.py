#!/usr/bin/env python3
"""Ephemeral external JBL QERC witness. Prints redacted JSON only."""

from __future__ import annotations

import asyncio
import base64
import hashlib
import json
import os
import platform
import time
import uuid
from datetime import datetime, timezone

from websockets.asyncio.client import connect


def pack(value: dict) -> bytes:
    encoded = json.dumps(value, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return len(encoded).to_bytes(4, "little") + encoded


def unpack(data: bytes | str) -> dict:
    if isinstance(data, str):
        data = data.encode("utf-8")
    if len(data) < 5:
        raise ValueError("QERC_FRAME_TOO_SHORT")
    length = int.from_bytes(data[:4], "little")
    if length != len(data) - 4:
        raise ValueError("QERC_LENGTH_MISMATCH")
    value = json.loads(data[4:].decode("utf-8"))
    if not isinstance(value, dict):
        raise ValueError("QERC_MESSAGE_NOT_OBJECT")
    return value


async def receive_until(ws, predicate, seconds: float = 8.0) -> dict:
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        message = unpack(await asyncio.wait_for(ws.recv(), deadline - time.monotonic()))
        if message.get("msg_type") == 3:
            await ws.send(pack(message))
            continue
        if predicate(message):
            return message
    raise TimeoutError("QERC_EXPECTED_MESSAGE_TIMEOUT")


def payload_object(message: dict) -> dict:
    payload = message.get("payload")
    if isinstance(payload, str):
        payload = json.loads(payload)
    if not isinstance(payload, dict):
        raise ValueError("QERC_PAYLOAD_NOT_OBJECT")
    return payload


async def read_gain(ws, device_uid: int, phase: str) -> int:
    message_id = f"wan-{phase}-{uuid.uuid4().hex}"
    await ws.send(pack({
        "msg_type": 4,
        "payload_msg_type": 4,
        "payload": {
            "msg_id": message_id,
            "content": {"uid": device_uid, "feature_list": ["microphone"]},
        },
    }))
    response = await receive_until(
        ws,
        lambda item: item.get("msg_type") == 4
        and item.get("payload_msg_type") == 5
        and payload_object(item).get("msg_id") == message_id,
    )
    content = payload_object(response).get("content")
    if not isinstance(content, dict) or not isinstance(content.get("microphone"), dict):
        raise ValueError("MICROPHONE_READBACK_MISSING")
    gain = content["microphone"].get("gain")
    if not isinstance(gain, int) or isinstance(gain, bool) or not 0 <= gain <= 100:
        raise ValueError("MICROPHONE_GAIN_INVALID")
    return gain


async def send_gain(ws, device_uid: int, gain: int, phase: str) -> None:
    await ws.send(pack({
        "msg_type": 4,
        "payload_msg_type": 2,
        "payload": {
            "msg_id": f"wan-{phase}-{uuid.uuid4().hex}",
            "content": {"uid": device_uid, "microphone": {"gain": gain}},
        },
    }))


async def main() -> int:
    started = datetime.now(timezone.utc)
    mode = os.environ["WITNESS_MODE"]
    tunnel_url = os.environ["TUNNEL_URL"].rstrip("/")
    pair_frame = base64.b64decode(os.environ["PAIR_FRAME_B64"], validate=True)
    if tunnel_url.startswith("https://"):
        websocket_url = "wss://" + tunnel_url.removeprefix("https://") + "/"
    elif tunnel_url.startswith("http://") and os.environ.get("LOCAL_PROTOCOL_SELFTEST") == "1":
        websocket_url = "ws://" + tunnel_url.removeprefix("http://") + "/"
    else:
        raise ValueError("TUNNEL_URL_SCHEME_INVALID")

    receipt = {
        "schema": "jbl.external-internet-witness.receipt.v1",
        "startedAt": started.isoformat(),
        "finishedAt": None,
        "mode": mode,
        "externalExecution": {
            "environment": "GITHUB_HOSTED_RUNNER" if os.environ.get("GITHUB_ACTIONS") == "true" else "LOCAL_PROTOCOL_SELFTEST",
            "platform": platform.platform(),
            "separateFromOwnerLan": os.environ.get("GITHUB_ACTIONS") == "true",
            "tunnelUrlPersistedOrPrinted": False,
            "pairingMaterialPersistedOrPrinted": False,
            "pairFrameSha256": hashlib.sha256(pair_frame).hexdigest().upper(),
        },
        "transport": {"websocketUpgradeObserved": False, "subprotocol": "quantum_rc"},
        "authorization": {"pairAccepted": False, "singleOwnerDeviceAccepted": False},
        "transition": {
            "setting": "microphone.gain",
            "baseline": None,
            "candidate": None,
            "candidateAttempted": False,
            "candidateIndependentReadbackObserved": False,
            "rollbackAttempted": False,
            "rollbackIndependentReadbackObserved": False,
            "terminalBaselineRestored": False,
        },
        "coverage": {
            "allIntermediateStatesObserved": False,
            "captureLoss": "UNKNOWN",
            "claimCeiling": "SEPARATE_INTERNET_HOST_OVER_OWNER_CREATED_TEMPORARY_TUNNEL",
        },
        "errors": [],
    }

    ws = None
    device_uid = None
    baseline = None
    candidate_attempted = False
    try:
        async with connect(
            websocket_url,
            subprotocols=["quantum_rc"],
            open_timeout=10,
            close_timeout=3,
            max_size=1024 * 1024,
        ) as ws:
            receipt["transport"]["websocketUpgradeObserved"] = True
            await ws.send(pair_frame)
            pair_response = await receive_until(ws, lambda item: item.get("msg_type") == 1)
            pair_payload = payload_object(pair_response)
            devices = pair_payload.get("device_list")
            if not isinstance(devices, list) or len(devices) != 1 or not isinstance(devices[0], dict):
                raise ValueError("PAIR_DEVICE_SET_NOT_SINGLE")
            receipt["authorization"]["pairAccepted"] = True
            receipt["authorization"]["singleOwnerDeviceAccepted"] = True
            device_uid = devices[0].get("uid")
            if not isinstance(device_uid, int) or isinstance(device_uid, bool):
                raise ValueError("DEVICE_UID_INVALID")
            pair_microphone = devices[0].get("microphone")
            if not isinstance(pair_microphone, dict):
                raise ValueError("PAIR_MICROPHONE_STATE_MISSING")
            baseline = await read_gain(ws, device_uid, "baseline")
            if baseline != pair_microphone.get("gain"):
                raise ValueError("PAIR_AND_GET_BASELINE_DISAGREE")
            receipt["transition"]["baseline"] = baseline

            if mode == "readonly":
                return_code = 0
            elif mode == "reversible-write":
                candidate = baseline - 1 if baseline > 0 else baseline + 1
                receipt["transition"]["candidate"] = candidate
                receipt["transition"]["candidateAttempted"] = True
                candidate_attempted = True
                try:
                    await send_gain(ws, device_uid, candidate, "candidate")
                    for attempt in range(4):
                        await asyncio.sleep(0.3)
                        if await read_gain(ws, device_uid, f"candidate-read-{attempt}") == candidate:
                            receipt["transition"]["candidateIndependentReadbackObserved"] = True
                            break
                    if not receipt["transition"]["candidateIndependentReadbackObserved"]:
                        raise RuntimeError("CANDIDATE_READBACK_NOT_OBSERVED")
                    return_code = 0
                finally:
                    receipt["transition"]["rollbackAttempted"] = True
                    try:
                        await send_gain(ws, device_uid, baseline, "rollback")
                        for attempt in range(6):
                            await asyncio.sleep(0.3)
                            if await read_gain(ws, device_uid, f"rollback-read-{attempt}") == baseline:
                                receipt["transition"]["rollbackIndependentReadbackObserved"] = True
                                receipt["transition"]["terminalBaselineRestored"] = True
                                break
                        if not receipt["transition"]["terminalBaselineRestored"]:
                            receipt["errors"].append("ROLLBACK_READBACK_NOT_OBSERVED")
                            return_code = 30
                    except Exception as error:
                        receipt["errors"].append("ROLLBACK_" + type(error).__name__)
                        return_code = 31
            else:
                raise ValueError("WITNESS_MODE_INVALID")
    except Exception as error:
        receipt["errors"].append(type(error).__name__)
        return_code = 20
    finally:
        receipt["finishedAt"] = datetime.now(timezone.utc).isoformat()
        print(json.dumps(receipt, indent=2, sort_keys=True))
    return return_code


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
