#!/usr/bin/env python3
# vim: set fileencoding=utf-8

# Knihovny Numpy a matplotlib
#
# Třetí demonstrační příklad:
# - vykreslení animovaného průběhů funkcí sin a cos
#   do jediného grafu

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

    # hodnoty na y-ové ose: první funkce
    y1 = np.sin(x + offset)

    # hodnoty na y-ové ose: druhá funkce
    y2 = np.cos(x - offset)

    # hodnoty na y-ové ose: součet funkcí
    y3 = y1 + y2

    # vykreslení průběhu funkce
    axis.plot(x, y1)
    axis.plot(x, y2)
    axis.plot(x, y3)
    axis.set_ylim(-2, 2)

    # konverze na objekt typu "frame"
    return mplfig_to_npimage(fig)


animation = VideoClip(make_frame, duration=DURATION)
animation.write_gif('sin_cos.gif', fps=FPS)
