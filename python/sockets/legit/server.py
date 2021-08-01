"""
server - Wait for a connection, echo incoming data to stdout, send stdin to
         clients.
"""

# built-in
import argparse
import socket
import sys
from typing import List


def main(argv: List[str] = None) -> int:
    """Program entry-point."""

    result = 0

    # fall back on command-line arguments
    command_args = sys.argv
    if argv is not None:
        command_args = argv

    desc = ("Listen for connections, print incoming messages, "
            + "send input back to clients.")
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=0,
        required=False,
        help="tcp port to listen on",
    )
    parsed = parser.parse_args(command_args[1:])

    # create the server socket
    with socket.create_server(("", parsed.port)) as sock:
        print(sock.getsockname())

        try:
            client, addr = sock.accept()
        except KeyboardInterrupt:
            return 0

        print("'{}' connected!".format(addr))
        while True:
            try:
                data = client.recv(1024)
                if not data:
                    break
                print(data.decode())
            except KeyboardInterrupt:
                break

    return result
