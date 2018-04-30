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


animation = VideoClip(make_frame, duration=DURATION)
animation.write_gif('polar.gif', fps=FPS)
