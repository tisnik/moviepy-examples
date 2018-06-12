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

import numpy as np
from numpy import pi
import pylab as plt
from colorsys import hls_to_rgb


# viz https://stackoverflow.com/a/20958684


def to_polar_form(z):
    """Prevod komplexniho cisla na goniometricky tvar."""
    r = np.abs(z)
    phi = np.angle(z)
    return r, phi


def polar_to_hls(r, phi):
    """Prevod polarnich souradnic do barvoveho prostoru HLS."""
    h = (phi + pi) / (2 * pi) + 0.5
    l = 1.0 - 1.0 / (1.0 + r ** 0.3)
    s = 0.8
    return h, l, s


def colorize(z):
    """Funkce pro prevod komplexni cislo -> HLS -> RGB."""
    r, phi = to_polar_form(z)

    h, l, s = polar_to_hls(r, phi)

    # prevod na n-tici
    c = np.vectorize(hls_to_rgb)(h, l, s)

    # zmena tvaru z (3,n,m) na (n,m,3)
    c = np.array(c)
    c = c.swapaxes(0, 2)
    return c


def show_graph(w):
    # obarveni vysledku
    img = colorize(w)

    # vykresleni grafu
    plt.imshow(img)
    plt.show()


# rozmery mrizky
N = 1000

# mrizka realnych cisel
x, y = np.ogrid[-5:5:N*1j, -5:5:N*1j]

# prevod na komplexni cisla
z = x + 1j*y

w = z
show_graph(w)

w = 1/z
show_graph(w)

w = z**2
show_graph(w)

w = z**z+z
show_graph(w)

w = (z**2+4)/(z**2-4)
show_graph(w)

w = np.tan(z)
show_graph(w)

w = np.tan(10/z)
show_graph(w)

w = np.sin(z**2)
show_graph(w)

w = 1/(z+1j)**2 + 1/(z-2)**2
show_graph(w)
