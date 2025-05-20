#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Teng jialin"
__id__ = 44702598


def PltRandom():
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.random.randn(20)
    y = np.random.randn(20)

    plt.scatter(x, y)

    plt.title("Random")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
    return


if __name__ == "__main__":
    PltRandom()
