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



def make_frame(t):
    """Deklarace callback funkce zavolane pri renderingu kazdeho snimku videa."""
    # offset v rozmezí 0 .. 2*Pi
    offset = 2 * np.pi * t / DURATION

    # hodnoty na y-ové ose
    y = np.sin(x + offset)

    fig = plt.figure(figsize=(1.0 * WIDTH / DPI, 1.0 * HEIGHT / DPI), dpi=DPI)

    plot = fig.add_subplot(111)

    # vykreslení průběhu funkce
    plot.plot(x, y)
    
    # konverze na objekt typu "frame"
    return mplfig_to_npimage(fig)


# vytvoreni video klipu
animation = VideoClip(make_frame, duration=DURATION)

# export videa do formatu GIF
animation.write_gif('sinus_C.gif', fps=FPS)
