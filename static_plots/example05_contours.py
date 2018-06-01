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
# - zobrazení kontur funkce typu z=f(x,y)

import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


delta = 0.1

# průběh nezávislé proměnné x
x = np.arange(-10.0, 10.0, delta)

# průběh nezávislé proměnné y
y = np.arange(-10.0, 10.0, delta)

# vytvoření dvou polí se souřadnicemi [x,y]
X, Y = np.meshgrid(x, y)

# vzdálenost od bodu [0,0]
R1 = np.sqrt(X*X+Y*Y)

# vzdálenost od bodu [3,3]
R2 = np.sqrt((X-3)*(X-3)+(Y-3)*(Y-3))

# výpočet funkce, kterou použijeme při vykreslování grafu
Z = np.sin(R1)-np.cos(R2)

# povolení zobrazení mřížky
plt.grid(True)

# vytvoření grafu s konturami funkce z=f(x,y)
plt.contour(X, Y, Z)

# zobrazení grafu
plt.show()
