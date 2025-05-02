#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Teng jialin"
__id__ = 44702598

import numpy as np
import matplotlib.pyplot as plt


period = np.pi
x = np.linspace(-period, period, 200)
sine = np.sin(x)
cosine = np.cos(x)
plt.figure()
plt.plot(x, sine, "r", label="sin(x)")
plt.plot(x, cosine, "b", label="cos(x)")

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
plt.legend()
plt.title("Function")
plt.show()
