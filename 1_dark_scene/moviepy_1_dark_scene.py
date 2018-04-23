#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from moviepy.editor import VideoClip
import numpy

WIDTH = 320
HEIGHT = 240


def make_frame(t):
    print("time: {t}".format(t=t))
    # vyplneni trojrozmerneho pole nulami
    frame = numpy.zeros((HEIGHT, WIDTH, 3))
    return frame


# vytvoreni video klipu
animation = VideoClip(make_frame, duration=10)

# export videa do formatu MPEG-4
animation.write_videofile("dark_scene.mp4", fps=24)

# export videa do formatu Ogg Video File
animation.write_videofile("dark_scene.ogv", fps=24)

# export videa do formatu GIF
animation.write_gif("dark_scene.gif", fps=24)
