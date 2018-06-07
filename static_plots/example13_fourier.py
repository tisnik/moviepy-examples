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
import matplotlib.pyplot as plt


def fourier_serie(x, order):
    """Vypocet Fourierovy rady zadaneho radu."""
    sum = 0
    for i in range(0, order):
        n = 2 * i + 1
        a = np.sin(x * n) / n
        sum += a
    return sum


# průběh nezávislé proměnné x
# (hodnoty na x-ové ose)
x = np.linspace(-4, 4, 500)

# funkce kterou aproximujeme
y = np.sin(x)

ys = np.vectorize(fourier_serie)

# Fourierova syntéza
N = 4

# vykresleni vsech prubehu Fourierovy rady
for order in range(1, N+1):
    approx = ys(x, order)
    plt.plot(x, approx, label='order {o}'.format(o=order))

# limity na ose y
plt.ylim([-1, 1])

# legenda grafu
plt.legend()

# zobrazení grafu
plt.show()
