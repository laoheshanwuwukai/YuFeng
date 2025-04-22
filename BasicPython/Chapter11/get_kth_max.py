#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Teng jialin"
__id__ = 44702598

import random
from typing import List


def GetKthMaxValue(nums: List[int], k: int) -> int:
    def separate(nums: List[int], k: int) -> int:
        # Separate nums into two lists based on a random pivot
        index = random.randint(0, len(nums)-1)
        value = nums[index]
        less, greater = [], []
        for n in nums:
            if n < value:
                less.append(n)
            elif n > value:
                greater.append(n)
        # If the k-th max is in the greater partition
        if k <= len(greater):
            return separate(greater, k)
        # If the k-th max is in the less partition
        elif k > len(nums)-len(less):
            return separate(less, k+len(less)-len(nums))
        else:
            return value
    return separate(nums, k)


if __name__ == "__main__":
    pass
