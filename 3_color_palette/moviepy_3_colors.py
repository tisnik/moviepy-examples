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

WIDTH = 256
HEIGHT = 256

index = 0


def make_frame(t):
    """Vytvoreni jednoho snimku videa."""
    global index
    print("time: {t}, index: {i}".format(t=t, i=index))

    # vyplneni trojrozmerneho pole nulami
    frame = numpy.zeros((HEIGHT, WIDTH, 3))

    # vyplneni barvovym prechodem
    for y in range(HEIGHT):
        for x in range(WIDTH):
            frame[y][x][0] = x
            frame[y][x][2] = y
            frame[y][x][1] = index
    index += 1
    return frame


# vytvoreni video klipu
animation = VideoClip(make_frame, duration=10)

# export videa do formatu Ogg Video File
animation.write_videofile("colors.ogv", fps=25)

# znovunastaveni pocitadla
index = 0

# export videa do formatu MPEG-4
animation.write_videofile("colors.mp4", fps=25)

# znovunastaveni pocitadla
index = 0

# export videa do formatu GIF
animation.write_gif("colors.gif", fps=25)
