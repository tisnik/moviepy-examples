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

from moviepy.editor import ImageClip, VideoClip, VideoFileClip, CompositeVideoClip
from moviepy.video.fx.all import *

# nacteni video klipu
clip = VideoFileClip('input_video.mp4', audio=False)

# aplikace rozmazani pohybem
blurred_clip = clip.fx(supersample, 1, 5)

# ulozeni video klipu do jineho souboru ve formatu Ogg/Theora
blurred_clip.write_videofile('12_motion_blur.ogv', bitrate='600000')
