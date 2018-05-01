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

from moviepy.editor import VideoClip
import numpy

WIDTH = 320
HEIGHT = 240

line = 0


def make_frame(t):
    global line
    print("time: {t}, line: {l}".format(t=t, l=line))

    # vyplneni trojrozmerneho pole nulami
    frame = numpy.zeros((HEIGHT, WIDTH, 3))

    # vykresleni jedine vodorovne usecky
    if line < HEIGHT:
        frame[line].fill(255)
        line += 1
    return frame


# vytvoreni video klipu
animation = VideoClip(make_frame, duration=10)

# export videa do formatu MPEG-4
animation.write_videofile("line.mp4", fps=24)

# znovunastaveni pocitadla
line = 0

# export videa do formatu Ogg Video File
animation.write_videofile("line.ogv", fps=24)

# znovunastaveni pocitadla
line = 0

# export videa do formatu GIF
animation.write_gif("line.gif", fps=24)
