# -*- coding: utf-8 -*-
"""
This class used for operate video

Author: Zhe Xiao
Contact: zhexiao27@gmail.com
    
Github: https://github.com/zhexiao/vcgif
"""

import subprocess
import re
import uuid
import os

from vcgif.GifAbstract import GifAbstract

class Conv(object):
    """
    Converter class, encapsulates formats and codecs.
    >>> c = Converter()1
    """

    def __init__(self, ffmpeg_path=None, ffprobe_path=None):
        """
        Initialize a new Converter object.
        """
        pass
    

class ZVideo(GifAbstract):
    """
        Video class
    """
    
    def __init__(self, **kwargs):
        super(ZVideo, self).__init__()

        """ video url """
        self._video = kwargs.pop('video') or self._video

        """ set start timestamp """
        self._start_timestamp = kwargs.pop('start_timestamp') or self._start_timestamp

        """ set gif duration """
        self._gif_duration = kwargs.pop('gif_duration') or self._gif_duration

        """ set gif frames per second """
        self._fps = kwargs.pop('fps') or self._fps

        """ set gif convert quality """
        self._quality = kwargs.pop('quality') or self._quality

        """ set target gif destination """
        self._destination = kwargs.pop('destination') or self._destination

        """ set gif name """
        self._gif_name = kwargs.pop('name') or self._gif_name
 
    def analysis(self):
        """ analysis video """
        try:
            result = subprocess.Popen(["ffprobe", self.video], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)

            for video_data in result.stdout.readlines():
                video_data = video_data.strip().decode('utf-8')

                # duration info
                if  video_data.startswith('Duration'):
                    self.duration = re.search('Duration: (.*?),', video_data).group(0).split(':',1)[1].strip(' ,')
                    self.bitrate = re.search("bitrate: (\d+ kb/s)", video_data).group(0).split(':')[1].strip()
                # video info
                elif video_data.startswith('Stream #0:') and 'Video:' in video_data:
                    self.video_info = {}
                    self.video_info['codec'], self.video_info['profile'] = [e.strip(' ,()') for e in re.search('Video: (.*? \(.*?\)),? ', video_data).group(0).split(':')[1].split('(')]
                    self.video_info['bitrate'] = re.search('(\d+ kb/s)', video_data).group(1)
                    self.video_info['fps'] = re.search('(\d+ fps)', video_data).group(1)
                    self.video_info['width'], self.video_info['height'] = re.search('([1-9]\d+x\d+)', video_data).group(1).split('x')
                # audio info
                elif video_data.startswith('Stream #0:') and 'Audio:' in video_data:
                    self.audio_info = {}
                    self.audio_info['codec'] = re.search('Audio: (.*?) ', video_data).group(1)
                    self.audio_info['frequency'] = re.search(', (.*? Hz),', video_data).group(1)
                    self.audio_info['bitrate'] = re.search(', (\d+ kb/s)', video_data).group(1)
        except Exception as e:
            print(e)

    def generate_gif(self):
        """ convert dispatch """
        
        # gif path
        self.gif_path = '{0}/{1}.gif'.format(self._destination, self._gif_name)

        if self._quality == 'high':
            self.generate_high_quality_gif()
        else:
            self.generate_low_quality_gif()

    def generate_high_quality_gif(self):
        """ generate high quality gif """
        palette="/tmp/{0}.png".format( str(uuid.uuid4()) )
        palette_command = 'ffmpeg -v warning -ss {0} -t {1} -i {2} -vf "fps={3},scale=320:-1:flags=lanczos,palettegen" -y {4}'.format(self._start_timestamp, self._gif_duration, self._video, self._fps, palette)

        subprocess.call(palette_command, shell=True,  stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)

        gif_command = 'ffmpeg -v warning -ss {0} -t {1} -i {2} -i {3} -lavfi "fps={4},scale=320:-1:flags=lanczos [x]; [x][1:v] paletteuse" -y {5}'.format(self._start_timestamp, self._gif_duration, self._video, palette, self._fps, self.gif_path)
        subprocess.call(gif_command, shell=True,  stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)

    def generate_low_quality_gif(self):
        """ generate low quality gif """
        command = 'ffmpeg -v warning -ss {0} -t {1} -i {2} -r {3} -vf scale=320:-1 -gifflags +transdiff -y {4} 2>&1'.format(self._start_timestamp, self._gif_duration, self._video, self._fps, self.gif_path)

        subprocess.call(command, shell=True,  stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)