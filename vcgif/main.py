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
            '-s', '--start',
            help='The start second of video file',
        )
        parser.add_argument(
            '-d', '--duration',
            help='The duration of output gif',
        )
        parser.add_argument(
            '-fps', '--fps',
            help='The frames per second of output gif',
        )
        parser.add_argument(
            '-q', '--quality',
            help='The quality of output file',
        )
        parser.add_argument(
            '-dest', '--destination',
            help='The destination path of output file ',
        )
        parser.add_argument(
            '-n', '--name',
            help='The output file name',
        )

        args = parser.parse_args()
    except Exception as e:
        parser.print_help()

    # bootstrap 
    GifBootstrap(args)

