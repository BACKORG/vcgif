# -*- coding: utf-8 -*-
"""
Abstract class for all gif
"""

# internal libs
import uuid
from abc import ABCMeta, abstractmethod

class GifAbstract(metaclass=ABCMeta):
    def __init__(self):
        self._video = None
        self._start_timestamp = 0
        self._gif_duration = 5
        self._fps = 15
        self._quality = 'low'
        self._destination = '.'
        self._gif_name = str(uuid.uuid4())

    @property
    def video(self):
        return self._video

    @video.setter
    def video(self, val):
        self._video = val

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

    @abstractmethod
    def generate_gif(self):
        """ All subclass need implement this function """
        pass
