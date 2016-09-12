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
            help='Video path',
        )
        parser.add_argument(
            '-p', '--picture',
            help='Picture path',
            nargs='+'
        )
        parser.add_argument(
            '-t', '--target',
            help='The output file destination path',
        )

        args = parser.parse_args()
    except Exception as e:
        parser.print_help()

    # bootstrap 
    GifBootstrap(args)

