"""
client - Connect to a server and send stdin over the connection.
"""

# built-in
import sys
from typing import List


def main(argv: List[str] = None) -> int:
    """Program entry-point."""

    result = 0

    # fall back on command-line arguments
    command_args = sys.argv
    if argv is not None:
        command_args = argv

    print(command_args)
    print(__name__)

    return result