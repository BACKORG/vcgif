# -*- coding: utf-8 -*-
"""
This is a bootstrap class

Author: Zhe Xiao
Contact: zhexiao27@gmail.com
    
Github: https://github.com/zhexiao/vcgif
"""

from vcgif.GifAbstract import GifAbstract

class GifBootstrap(GifAbstract):
    
    def __init__(self, args):
        print(args.video)
