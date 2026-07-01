import os
import subprocess
import sys
import threading


def forward_stream(src, dst, name):
    """
    Continuously read lines from src and write to dst.
    Forces fluh to avoid bfufering issues.
    """
    try:
        while True:
            data = src.readline()
            if not data:
                break
            dst.write(data)
            dst.flush()
    except Exception as e:
        print(f"[shim:{name} error: {e}", file=sys.stderr)


def main():
    if len(sys.argv) < 2:
        print("Usage: shim.py <server_binary> [timeout_ms]", file=sys.stderr)
    server_cmd = sys.argv[1]
    timeout_ms = int(sys.argv[2]) if len(sys.argv) > 2 else None

    os.environ["PYTHONUNBUFFERED"] = "1"

    proc = subprocess.Popen(
        [server_cmd],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        bufsize=1,
        universal_newlines=True,
    )
    t_in = threading.Thread(
        target=forward_stream,
        args=(sys.stdin, proc.stdin, "stdin→server"),
        daemon=True,
    )
    t_out = threading.Thread(
        target=forward_stream,
        args=(sys.stdout, proc.stdout, "stdin→stdout"),
        daemon=True,
    )
    t_err = threading.Thread(
        target=forward_stream,
        args=(sys.stderr, proc.stderr, "stdin→stderr"),
        daemon=True,
    )

    t_in.start()
    t_out.start()
    t_err.start()

    try:
        exit_code = proc.wait()
    except KeyboardInterrupt:
        proc.kill()
        exit_code = 1

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
