#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = "Teng jialin"
__id__ = 44702598

'''
usage:
    pytest test_get_kth_max.py -v
'''

from get_kth_max import GetKthMaxValue
import pytest
import random


@pytest.mark.parametrize("test_rounds", [100])
def test_GetKthMaxValue(test_rounds: int):
    minlen, maxlen = 1, 200
    minvalue, maxvalue = -100, 100

    for _ in range(test_rounds):
        nums = [random.randint(minvalue, maxvalue)
                for _ in range(random.randint(minlen, maxlen))]
        k = random.randint(1, len(nums))

        # NOTE: Avoid modifying nums in place
        # test_result = GetKthMaxValue(nums, k)
        test_result = GetKthMaxValue(nums[:], k)
        # ans = sorted(nums)[len(nums)-k]
        ans = sorted(nums)[-k]

        assert test_result == ans, (
            f"Test failed!\n"
            f"nums: {nums}\n"
            f"k: {k}\n"
            f"Expected: {ans}, Got: {test_result}"
        )
