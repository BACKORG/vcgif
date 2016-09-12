# -*- coding: utf-8 -*-
"""
This is a bootstrap class

Author: Zhe Xiao
Contact: zhexiao27@gmail.com
    
Github: https://github.com/zhexiao/vcgif
"""

from vcgif.GifAbstract import GifAbstract
from vcgif.Video import Video

class GifBootstrap(GifAbstract):
    
    def __init__(self, args):
        self.args = args
        self.dispatch()

    def dispatch(self):
        if self.args.video is not None:
            Video(self.args)
