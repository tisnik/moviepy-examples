#!/usr/bin/env python

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
# - Lorenzův atraktor

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage


# parametry obrázků / rámců
WIDTH = 400
HEIGHT = 300
DPI = 100

# parametry animace
DURATION = 16
FPS = 8


# funkce pro výpočet dalšího bodu Lorenzova atraktoru
def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

# krok (změna času)
dt = 0.01


fig = plt.figure(figsize=(1.0 * WIDTH / DPI, 1.0 * HEIGHT / DPI), dpi=DPI)
axis = fig.add_subplot(111, projection="3d")

max = 0

def make_frame(t):
    axis.clear()

    global max

    # celkový počet vypočtených bodů na Lorenzově atraktoru
    n = 10 + max * 10

    max += 1

    # prozatím prázdné pole připravené pro výpočet
    x = np.zeros((n,))
    y = np.zeros((n,))
    z = np.zeros((n,))

    # počáteční hodnoty
    x[0], y[0], z[0] = (0., 1., 1.05)

    # vlastní výpočet atraktoru
    for i in range(n-1):
        x_dot, y_dot, z_dot = lorenz(x[i], y[i], z[i])
        x[i+1] = x[i] + x_dot * dt
        y[i+1] = y[i] + y_dot * dt
        z[i+1] = z[i] + z_dot * dt

    ax = fig.gca(projection='3d')

    ax.set_axis_off()

    ax.plot(x, y, z)

    # konverze na objekt typu "frame"
    return mplfig_to_npimage(fig)


animation = VideoClip(make_frame, duration=DURATION)
# animation.write_gif('lorenz1.gif', fps=FPS)
animation.write_videofile('lorenz1.ogv', fps=FPS, progress_bar=True)
