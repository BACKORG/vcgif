# -*- coding: utf-8 -*-
"""
Abstract class for all gif
"""

# internal libs
import os
from abc import ABCMeta, abstractmethod, abstractproperty

class GifAbstract(metaclass=ABCMeta):
  
    @property
    def quality_level(self):
        """ gif quality """
        return self._quality_level

    @quality_level.setter
    def quality_level(self, value):
        self._quality_level = value