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
# - zobrazení 3D grafu funkce typu z=f(x,y)

from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y] 
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R = np.sqrt(X*X+Y*Y)

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R)/R

# zobrazení 3D grafu formou plochy
ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# zobrazení grafu
plt.show()

