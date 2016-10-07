# -*- coding: utf-8 -*-
import uuid
from abc import ABCMeta, abstractmethod

class GifAbstract(metaclass=ABCMeta):
    """Gif Abstract Class

    This class is gif abstract class, all convert class(video or picture) should
    inherit from this class.
    
    Args:
        * ``video`` (`string`): video path.
        * ``start_timestamp`` (`int`): set the start timestamp of the video.
        * ``gif_duration`` (`int`): set the gif duration length.
        * ``fps`` (`int`): set the gif file frame rate.
        * ``quality`` (`string:high`, `string:low`): set the gif file quality.
        * ``destination`` (`string`): set the gif file output path.
        * ``gif_name`` (`string`): set the gif filename.
        
    """
    
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
        """
        string: return video path.
        
        :param val: video path
        """
        return self._video

    @video.setter
    def video(self, val):
        """void: set video path."""
        self._video = val

    @property
    def start_timestamp(self):
        """
        int: return start timestamp length.
        
        :param val: timestamp length
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, val):
        """void: set start timestamp length."""
        self._start_timestamp = val

    @property
    def gif_duration(self):
        """int: return gif duration length."""
        return self._gif_duration

    @gif_duration.setter
    def gif_duration(self, val):
        """void: set gif duration length."""
        self._gif_duration = val

    @property
    def fps(self):
        """int: return gif fps number."""
        return self._fps

    @fps.setter
    def fps(self, val):
        """void: set gif fps."""
        self._fps = val

    @property
    def quality(self):
        """string: return gif file quality."""
        return self._quality

    @quality.setter
    def quality(self, val):
        """void: set gif file quality."""
        self._quality = val

    @property
    def destination(self):
        """string: return gif output file path."""
        return self._destination

    @destination.setter
    def destination(self, val):
        """void: set gif output file path."""
        self._destination = val

    @property
    def name(self):
        """string: return gif output filename."""
        return self._gif_name

    @name.setter
    def name(self, val):
        """void: set gif output filename."""
        self._gif_name = val

    @abstractmethod
    def generate_gif(self):
        """Abstract method for generate gif 
        
        All class should implement this method, even using `pass`. 
        
        """
        pass
