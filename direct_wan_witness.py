import json
import os
import socket
import time

host = os.environ["TARGET_HOST"]
started = time.time()
result = {
    "schema": "jbl.direct-wan-tcp-witness.v1",
    "runner": "github-hosted-ubuntu",
    "targetHostRedacted": True,
    "targetPort": 57120,
    "attemptCount": 1,
    "payloadBytesSent": 0,
}

try:
    with socket.create_connection((host, 57120), timeout=8):
        result["tcpConnected"] = True
        result["outcome"] = "TCP_CONNECTION_ESTABLISHED_NO_PAYLOAD"
except (TimeoutError, socket.timeout):
    result["tcpConnected"] = False
    result["outcome"] = "TIMEOUT_WITHIN_BOUND_WINDOW"
except OSError as exc:
    result["tcpConnected"] = False
    result["outcome"] = f"OS_ERROR_{exc.errno}"

result["elapsedMs"] = round((time.time() - started) * 1000)
print(json.dumps(result, sort_keys=True))
