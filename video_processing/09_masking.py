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

from moviepy.editor import ImageClip, VideoFileClip, CompositeVideoClip
from moviepy.video.fx.all import *

# nacteni video klipu
clip = VideoFileClip('input_video.mp4', audio=False)

# nacteni masky
mask = ImageClip('mask.png', ismask=True)

# aplikace masky
final = CompositeVideoClip([clip.set_mask(mask)])

# ulozeni video klipu do jineho souboru ve formatu Ogg/Theora
final.write_videofile('09_output_masked.ogv', bitrate='600000')
