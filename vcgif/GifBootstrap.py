# -*- coding: utf-8 -*-
"""
This is a bootstrap class

Author: Zhe Xiao
Contact: zhexiao27@gmail.com
    
Github: https://github.com/zhexiao/vcgif
"""

from vcgif.GifFactory import GifFactory

class GifBootstrap:
    
    def __init__(self, args):
        self.args = args
        self.instance = GifFactory.factory(self.args)
        self.dispatch()

    def dispatch(self):
        # self.instance.generate_gif()
        self.instance.analysis()
        # print(self.instance.video_info)
