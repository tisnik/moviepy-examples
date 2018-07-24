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

# Knihovny Numpy a matplotlib
#
# - základní polární animovaný graf

import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

# parametry obrázků / rámců
WIDTH = 400
HEIGHT = 400
DPI = 100

# parametry animace
DURATION = 10
FPS = 15

fig = plt.figure(figsize=(1.0 * WIDTH / DPI, 1.0 * HEIGHT / DPI), dpi=DPI)
axis = fig.add_subplot(111, projection="polar")


def make_frame(t):
    """Deklarace callback funkce zavolane pri renderingu kazdeho snimku videa."""
    axis.clear()

    # offset v rozmezí 0 .. 2*Pi
    offset = 2 * np.pi * t / DURATION

    # úhel v polárním grafu
    theta = np.linspace(0.01 + offset, 2*np.pi + offset, 150)

    # vzdálenost od středu
    radius = np.log(theta)

    # vykreslení průběhu funkce
    # v polárním grafu
    axis.plot(theta, radius)

    # konverze na objekt typu "frame"
    return mplfig_to_npimage(fig)


# vytvoreni video klipu
animation = VideoClip(make_frame, duration=DURATION)

# export videa do formatu GIF
animation.write_gif('polar.gif', fps=FPS)
