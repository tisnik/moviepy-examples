#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import numpy as np
import matplotlib.pyplot as plt


def taylor_series(x, order):
    """Výpočet aproximace hodnoty funkce pomocí Taylorovy řady."""
    a = x
    sum = a
    for i in range(1, order):
        a *= -1 * x**2 / ((2 * i) * (2 * i + 1))
        sum += a
    return sum


# průběh nezávislé proměnné x
# (hodnoty na x-ové ose)
x = np.linspace(-20, 20, 500)

# funkce kterou aproximujeme
y = np.sin(x)

# vykreslení původní funkce
plt.plot(x, y, label='sin(x)')

ys = np.vectorize(taylor_series)

# aproximace
N = 10

for order in range(1, N+1):
    approx = ys(x, order)
    plt.plot(x, approx, label='order {o}'.format(o=order))

# limity na ose y
plt.ylim([-3, 3])

# legenda grafu
plt.legend()

# zobrazení grafu
plt.show()
