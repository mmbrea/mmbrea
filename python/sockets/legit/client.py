"""
client - Connect to a server and send standard input over the connection.
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

    desc = "Connect to a server and send messages from standard input."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("host", type=str, help="host to connect to")
    parser.add_argument("port", type=int, help="port to connect to on host")
    parsed = parser.parse_args(command_args[1:])

    # connect to the server
    with socket.create_connection((parsed.host, parsed.port)) as sock:
        while True:
            try:
                data = input("=> ")
                sock.send(data.encode())
            except (KeyboardInterrupt, ConnectionAbortedError):
                break

    return result
