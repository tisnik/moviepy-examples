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
# Demonstrační příklad:
# - vykreslení rozkladu obdélníkového signálu na sinusové průběhy

import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage


# parametry animace
DURATION = 20
FPS = 0.8


def fourier_serie(x, order):
    sum = 0
    for i in range(0, order):
        n = 2 * i + 1
        a = np.sin(x * n) / n
        sum += a
    return sum


# průběh nezávislé proměnné x
# (hodnoty na x-ové ose)
x = np.linspace(-4, 4, 500)

# funkce kterou aproximujeme
y = np.sin(x)

ys = np.vectorize(fourier_serie)

# vytvoření objektu reprezentujícího průběh funkce
fig, axis = plt.subplots()

# zde začínáme od nuly!
# viz: https://github.com/Zulko/moviepy/issues/155
order = 0

def make_frame(t):
    axis.clear()

    # Fourierova syntéza
    global order
    approx = ys(x, order)

    axis.plot(x, approx, label='order {o}'.format(o=order))
    order += 1

    # limity na ose y
    axis.set_ylim([-1, 1])
    axis.legend()

    # konverze na objekt typu "frame"
    return mplfig_to_npimage(fig)


animation = VideoClip(make_frame, duration=DURATION)
animation.write_gif('fourier_square_wave.gif', fps=FPS)
