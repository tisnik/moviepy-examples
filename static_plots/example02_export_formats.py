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
# Druhý demonstrační příklad:
# - vykreslení průběhu funkce sin
# - uložení grafu do různých typů souboru

import numpy as np
import matplotlib.pyplot as plt

# hodnoty na x-ové ose
x = np.linspace(0, 2*np.pi, 100)

# hodnoty na y-ové ose
y = np.sin(x)

# vykreslit průběh funkce
plt.plot(x, y)

# popis os
plt.xlabel("x")
plt.ylabel("sin(x)")

# vykreslení a uložení grafu do různých typů souborů
plt.savefig("example02.png")
plt.savefig("example02.pdf")
plt.savefig("example02.eps")
plt.savefig("example02.ps")
plt.savefig("example02.svg")

# zobrazení grafu
plt.show()
