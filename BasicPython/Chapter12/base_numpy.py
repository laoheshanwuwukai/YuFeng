#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import numpy as np

a = np.array(
    [1, 2, 3]
)
b = np.array(
    [[1, 2, 3],
     [4, 5, 6]]
)
c = np.array(
    [[[1, 2, 3],
     [4, 5, 6]]
     ]
)

print(a)
print(a.ndim)
print(a.shape)
print(a.size)  # n*m
print(a.dtype)

print(b)
print(b.ndim)
print(b.shape)
print(b.size)  # n*m
print(b.dtype)

print(c)
print(c.ndim)
print(c.shape)
print(c.size)  # n*m
print(c.dtype)
