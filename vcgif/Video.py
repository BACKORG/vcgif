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

class Video:
    def __init__(self, video, **kwargs):
        """ set start timestamp """
        self._start_timestamp = kwargs.pop('start_timestamp', 0)

        """ set gif duration """
        self._gif_duration = kwargs.pop('gif_duration', 10)

        """ set gif frames per second """
        self._fps = kwargs.pop('fps', 12)

        """ set gif convert quality """
        self._quality = kwargs.pop('quality', 'low')

        """ set target gif destination """
        self._destination = kwargs.pop('destination', '.')

        """ set gif name """
        self._gif_name = kwargs.pop('name', str(uuid.uuid4()))

        """ video property """
        self.video = video

    @property
    def start_timestamp(self):
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, val):
        self._start_timestamp = val

    @property
    def gif_duration(self):
        return self._gif_duration

    @gif_duration.setter
    def gif_duration(self, val):
        self._gif_duration = val

    @property
    def fps(self):
        return self._fps

    @fps.setter
    def fps(self, val):
        self._fps = val

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, val):
        self._quality = val

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, val):
        self._destination = val

    @property
    def name(self):
        return self._gif_name

    @name.setter
    def name(self, val):
        self._gif_name = val

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

    def convert_gif(self):
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
        palette_command = 'ffmpeg -v warning -ss {0} -t {1} -i {2} -vf "fps=12,scale=320:-1:flags=lanczos,palettegen" -y {3}'.format(self.start_timestamps, self.gif_duration, self.video_fullpath, palette)

        subprocess.call(palette_command, shell=True,  stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)

        gif_command = 'ffmpeg -v warning -ss {0} -t {1} -i {2} -i {3} -lavfi "fps=12,scale=320:-1:flags=lanczos [x]; [x][1:v] paletteuse" -y {4}'.format(self.start_timestamps, self.gif_duration, self.video_fullpath, palette, self.gif_fullpath)
        subprocess.call(gif_command, shell=True,  stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)

    def generate_low_quality_gif(self):
        """ generate low quality gif """
        command = 'ffmpeg -v warning -ss {0} -t {1} -i {2} -r 12 -vf scale=320:-1 -gifflags +transdiff -y {3} 2>&1'.format(self._start_timestamp, self._gif_duration, self.video, self.gif_path)

        subprocess.call(command, shell=True,  stdout=open(os.devnull, "w"), stderr=subprocess.STDOUT)