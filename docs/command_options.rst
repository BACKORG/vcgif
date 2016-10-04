Command Option Lists
====================
This docs is aim to describe all existing options in the vcgif.

Video path
----------
The option ``-v or --video`` is used for indicate the video path.

.. note:: vcgif -v /var/www/video.mp4

Picture path
------------
The option ``-p or --picture`` is used for indicate your picture path, you can have multiple pictures
path exist.

.. note:: vcgif -p /var/www/pic1.png /var/www/pic2.png

Gif start time
--------------
The option ``-st or --start-timestamp`` is mark the start time from the video. picture is not require 
use this option.

**default value is 0**

.. note:: vcgif -st 10

Gif duration time
-----------------
The option ``-gd or --gif-duration`` is the display time for your gif.

**default value is 5**

.. note:: vcgif -gd 10

Frames per second
-----------------
The option ``-fps or --fps`` is for the frames per second of output gif.

**default value is 15**

.. note:: vcgif -fps 20

Gif quality
-----------------
The option ``-q or --quality`` is indicate your gif quality.

**default value is ``low``, you can use ``high`` to generate high quality gif**

.. note:: vcgif -q high


Gif file destination
---------------------
The option ``-dest or --destination`` is indicate your output file path.

**default value is ``.``**

.. note:: vcgif -dest /var/www/gif

Gif file name
---------------------
The option ``-n or --name`` is your gif file name.

**default value is uuid random string** *(do not need add file extension at the end)* 

.. note:: vcgif -n my_gif








