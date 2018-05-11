#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# Knihovny Numpy a matplotlib
#
# Demonstrační příklad:
# - vykreslení postupné aproximace funkce sin

import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage


# parametry animace
DURATION = 20
FPS = 0.8


def taylor_series(x, order):
    u"""Výpočet aproximace hodnoty funkce pomocí Taylorovy řady."""
    a = x
    sum = a
    for i in range(1, order):
        a *= -1 * x**2 / ((2 * i) * (2 * i + 1))
        sum += a
    return sum


# průběh nezávislé proměnné x
# (hodnoty na x-ové ose)
x = np.linspace(-20, 20, 500)

# funkce kterou aproximujeme
y = np.sin(x)

ys = np.vectorize(taylor_series)

# vytvoření objektu reprezentujícího průběh funkce
fig, axis = plt.subplots()

# zde začínáme od nuly!
# viz: https://github.com/Zulko/moviepy/issues/155
order = 0


def make_frame(t):
    axis.clear()

    # vykreslení původní funkce
    axis.plot(x, y, label='sin(x)')

    # aproximace
    global order
    approx = ys(x, order)

    axis.plot(x, approx, label='order {o}'.format(o=order))
    order += 1

    # limity na ose y
    axis.set_ylim([-3, 3])
    axis.legend()

    # konverze na objekt typu "frame"
    return mplfig_to_npimage(fig)


animation = VideoClip(make_frame, duration=DURATION)
animation.write_gif('taylor_sinus.gif', fps=FPS)
# animation.write_videofile('taylor_sinus.ogv', fps=FPS)
