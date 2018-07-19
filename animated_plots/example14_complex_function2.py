#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import numpy as np
from numpy import pi
import pylab as plt
from colorsys import hls_to_rgb
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage


# viz https://stackoverflow.com/a/20958684


def to_polar_form(z):
    """Prevod komplexniho cisla na goniometricky tvar."""
    r = np.abs(z)
    phi = np.angle(z) 
    return r, phi


def polar_to_hls(r, phi):
    """Prevod na HLS."""
    h = (phi + pi)  / (2 * pi) + 0.5
    l = 1.0 - 1.0/(1.0 + r**0.3)
    s = 0.8
    return h, l, s


def colorize(z):
    """Funkce pro prevod complex -> HLS -> RGB."""
    r, phi = to_polar_form(z)

    h, l, s = polar_to_hls(r, phi)

    # prevod na n-tici
    c = np.vectorize(hls_to_rgb) (h,l,s)

    # zmena tvaru z (3,n,m) na (n,m,3)
    c = np.array(c)
    c = c.swapaxes(0,2) 
    return c


# parametry animace
DURATION = 10
FPS = 10

# rozmery mrizky
N = 400

# mrizka realnych cisel
x, y = np.ogrid[-4:4:N*1j, -4:4:N*1j]

# prevod na komplexni cisla
z = x + 1j*y

fig = plt.figure(figsize=(20,20))

plt.subplot(111)

subplot = fig.add_subplot(111)


def make_frame(t):
    """Deklarace callback funkce zavolane pri renderingu kazdeho snimku videa."""
    power = 5 * t / DURATION - 2

    w = 1/(z+2j)**power + 1/(z-2)**power
    img = colorize(w)

    subplot.imshow(img)

    # konverze na objekt typu "frame"
    return mplfig_to_npimage(fig)


# vytvoreni video klipu
animation = VideoClip(make_frame, duration=DURATION)

# export videa do formatu Ogg/Vorbis
animation.write_videofile('complex2.ogv', fps=FPS, progress_bar=True, bitrate="800000")
