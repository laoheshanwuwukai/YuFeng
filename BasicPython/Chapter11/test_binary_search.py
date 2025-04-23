#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

__author__ = "Teng jialin"
__id__ = 44702598
'''
usage:
    pytest test_binary_search.py -v
'''

import pytest
from random import randint
from binary_search import binary_search


@pytest.mark.parametrize("_", range(10))
def test_binary_search_random(_):
    min_len = 1
    max_len = 30
    min_value = -100
    max_value = 100
    nums = [randint(min_value, max_value)
            for _ in range(randint(min_len, max_len))]
    random_index = randint(0, len(nums)-1)
    target = nums[random_index]

    test_result = binary_search(nums, target)
    nums.sort()
    expected_result = nums.index(target)
    assert test_result == expected_result, (
        f"Test failed!\n"
        f"nums: {nums}\n"
        f"target: {target}\n"
        f"Expected: {expected_result}, Got: {test_result}"
    )


@pytest.mark.parametrize("nums, target, expected", [
    # 基本情况
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 1, 0),
    ([1, 2, 3, 4, 5], 5, 4),

    # target 是最大或最小元素
    ([1, 2, 3, 4, 5], 0, -1),
    ([1, 2, 3, 4, 5], 6, -1),

    # 有重复元素，返回第一个出现的位置
    ([1, 2, 2, 2, 3], 2, 1),
    ([5, 5, 5, 5, 5], 5, 0),

    # 不存在的元素
    ([1, 3, 5, 7], 4, -1),
    ([10, 20, 30], 15, -1),

    # 空数组
    ([], 1, -1),

    # 单个元素
    ([1], 1, 0),
    ([1], 0, -1),

    # 非升序数组，测试是否内部排序
    ([9, 7, 5, 3, 1], 5, 2),

    # 大量重复元素，target 不存在
    ([2] * 1000, 3, -1),

])
def test_binary_search_given_datas(nums, target, expected):
    assert binary_search(nums, target) == expected
