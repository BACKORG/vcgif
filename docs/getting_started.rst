Getting Started
===============
This document will show you how to get up and running with vcgif.

Requirement
---------------

Python3 and pip3 are required for install vcgif.

.. code-block:: bash

   # update system package
   $ sudo apt-get update

   # install python3 and pip3
   $ sudo apt-get install python3 python3-pip

FFmpeg is required for process video.

.. code-block:: bash
    
    $ sudo add-apt-repository ppa:mc3man/trusty-media
    $ sudo apt-get update
    $ sudo apt-get install ffmpeg

Install
---------------
After you match the requirements, you can install vcgif directly from PyPI.

.. code-block:: bash

   $ sudo pip3 install vcgif

Test
----------
Open your command and running the following code, you will see a list of helps from vcgif.

.. code-block:: bash
    
    $ vcgif -h