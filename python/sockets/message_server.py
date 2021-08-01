#!/usr/bin/env python

"""
Run the message server.
"""

# built-in
import sys

# internal
from legit.server import main


if __name__ == "__main__":
    sys.exit(main(sys.argv))
