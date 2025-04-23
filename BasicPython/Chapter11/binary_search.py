#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Teng jialin"
__id__ = 44702598

from typing import List


def binary_search(origin_nums: List[int], target: int) -> int:
    '''
    return first index if find else -1
    '''
    nums = sorted(origin_nums)
    left, right = 0, len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            result = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
