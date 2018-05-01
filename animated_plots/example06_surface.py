# Knihovny Numpy a matplotlib
#
# - zobrazení 3D grafu funkce typu z=f(x,y)

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

# parametry obrázků / rámců
WIDTH = 400
HEIGHT = 300
DPI = 100

# parametry animace
DURATION = 4
FPS = 10

fig = plt.figure(figsize=(1.0 * WIDTH / DPI, 1.0 * HEIGHT / DPI), dpi=DPI)
axis = fig.add_subplot(111, projection="3d")

delta = 0.1


def make_frame(t):
    axis.clear()

    # offset v rozmezí 0 .. 2*Pi
    offset = 2.0 * np.pi * t / DURATION

    # průběh nezávislé proměnné x
    x = np.arange(-10.0, 10.0, delta)

    # průběh nezávislé proměnné y
    y = np.arange(-10.0, 10.0, delta)

    # vytvoření dvou polí se souřadnicemi [x,y]
    X, Y = np.meshgrid(x, y)

    # vzdálenost od bodu [0,0]
    R = np.sqrt(X*X+Y*Y) + offset

    # výpočet funkce, kterou použijeme při vykreslování grafu
    Z = np.sin(R)/R

    # zobrazení 3D grafu
    axis.set_axis_off()
    axis.margins(0, 0, 0)
    axis.plot_wireframe(X, Y, Z, rstride=7, cstride=7)
    axis.get_xaxis().set_visible(False)

    axis.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=cm.coolwarm,
                      linewidth=0, antialiased=False)

    # konverze na objekt typu "frame"
    return mplfig_to_npimage(fig)


animation = VideoClip(make_frame, duration=DURATION)
animation.write_gif('wireframe.gif', fps=FPS)