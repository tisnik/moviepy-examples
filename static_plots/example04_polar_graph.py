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
# - základní polární graf

import numpy as np
import matplotlib.pyplot as plt

# úhel v polárním grafu
theta = np.linspace(0.01, 2*np.pi, 150)

# vzdálenost od středu
radius = np.log(theta)

ax = plt.subplot(111, projection="polar")

# vykreslit průběh funkce
# v polárním grafu
ax.plot(theta, radius)

# zobrazení grafu
plt.show()
