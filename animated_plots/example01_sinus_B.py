#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# Knihovny Numpy a matplotlib
#
# První demonstrační příklad:
# - vykreslení animovaného průběhu funkce sin

import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

# parametry obrázků / rámců
WIDTH = 400
HEIGHT = 300
DPI = 100

# parametry animace
DURATION = 10
FPS = 15

# hodnoty na x-ové ose
x = np.linspace(0, 2 * np.pi, 100)

# vytvoření objektu reprezentujícího průběh funkce
# + nastavení rozlišení obrázku (resp. jednotlivých rámců)
fig, axis = plt.subplots(figsize=(1.0 * WIDTH / DPI, 1.0 * HEIGHT / DPI), dpi=DPI)


def make_frame(t):
    axis.clear()

    # offset v rozmezí 0 .. 2*Pi
    offset = 2 * np.pi * t / DURATION

    # hodnoty na y-ové ose
    y = np.sin(x + offset)

    # vykreslení průběhu funkce
    axis.plot(x, y)

    # konverze na objekt typu "frame"
    return mplfig_to_npimage(fig)


animation = VideoClip(make_frame, duration=DURATION)
animation.write_gif('sinus_B.gif', fps=FPS)
