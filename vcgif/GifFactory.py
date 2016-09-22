"""
Factory for initial class
"""
from vcgif.ZVideo import ZVideo

class GifFactory:

    @staticmethod
    def factory(args):
        if args['video'] is not None:
            return ZVideo(**args)
