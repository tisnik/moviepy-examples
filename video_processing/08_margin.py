#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2018  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

from moviepy.editor import VideoClip, VideoFileClip
from moviepy.video.fx.all import *
import numpy

# nacteni video klipu
clip = VideoFileClip('input_video.mp4', audio=False).margin(20)

# ulozeni video klipu do jineho souboru
clip.write_videofile('08_output_with_margin.ogv', bitrate='700000')
