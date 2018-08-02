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

import os
import glob
from moviepy.editor import ImageClip, concatenate_videoclips

fps = 10
frame_duration = 2

# ziskani serazeneho seznamu souboru *.png
base_dir = os.path.realpath(".")
file_list = glob.glob('*.png')
file_list_sorted = sorted(file_list)

# vytvoreni sady objektu typu ImageClip
clips = [ImageClip(filename).set_duration(frame_duration)
         for filename in file_list_sorted]

# kompozice vsech kratkych video klipu
concat_clip = concatenate_videoclips(clips, method="compose")

# ulozeni vysledneho video klipu do souboru ve formatu Ogg/Theora
concat_clip.write_videofile("test.ogv", fps=fps)
