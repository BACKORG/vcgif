#!/usr/bin/python
"""
This module contains `main` method plus related subroutines.
`main` is executed as the command line ``vcgif`` program and takes care of
parsing options and commands
"""

import argparse

from vcgif.GifBootstrap import GifBootstrap

def main():
    try:
        parser = argparse.ArgumentParser(description='Gif generate from video or picture.')

        parser.add_argument(
            '-v', '--video',
            help='Convert video entity path',
        )

        parser.add_argument(
            '-p', '--picture',
            help='Convert picture entity path',
            nargs='+'
        )

        args = parser.parse_args()
    except Exception as e:
        parser.print_help()

    # bootstrap 
    GifBootstrap(args)

