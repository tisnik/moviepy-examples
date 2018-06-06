#!/usr/bin/env python
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
# - zobrazení 3D grafu funkce typu [x,y,z]=f(t)

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# nezávislá proměnná
t = np.arange(0, 8*np.pi, 0.1)

# vzdálenost od osy spirály
r = 10.0/(t+4)

# výpočet souřadnic [x,y,z]) pro každé t
x = r*np.cos(t)
y = r*np.sin(t)
z = t

fig = plt.figure()
ax = fig.gca(projection='3d')

# vykreslení grafu
ax.plot(x, y, z)

# zobrazení grafu
plt.show()
