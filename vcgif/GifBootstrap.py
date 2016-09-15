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
            media = Video(self.args.video)

            if self.args.start is not None:
                media.start_timestamp = self.args.start

            if self.args.duration is not None:
                media.gif_duration = self.args.duration

            if self.args.fps is not None:
                media.fps = self.args.fps

            if self.args.quality is not None:
                media.quality = self.args.quality

            if self.args.destination is not None:
                media.destination = self.args.destination

            if self.args.name is not None:
                media.name = self.args.name 

        

            media.convert_gif()
