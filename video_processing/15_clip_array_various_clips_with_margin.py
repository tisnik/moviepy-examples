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
from moviepy.editor import clips_array
from moviepy.video.fx.all import *

# nacteni video klipu
clip = VideoFileClip('input_video.mp4', audio=False).margin(10)

# nacteni masky
mask = ImageClip('mask.png', ismask=True)

# aplikace masky
clip2 = CompositeVideoClip([clip.set_mask(mask)])

# aplikace rozmazani pohybem
clip3 = clip.fx(supersample, 0.25, 10)

# aplikace rozmazani pohybem
clip4 = clip.fx(supersample, 1, 5)

final_clip = clips_array([[clip, clip2],
                          [clip3, clip4]])

# ulozeni video klipu do jineho souboru ve formatu Ogg/Theora
final_clip.write_videofile('15_clip_array_with_margin.ogv', bitrate='800000')
