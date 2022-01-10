# -*- coding:utf-8 -*-
__author__: 'Rvelamen'
__data__ = '2021/9/8 7:13'


class Solution:
    def twoSum(self, nums, target):
        _dict = {}
        for _, _items in enumerate(nums):
            if target - _items in _dict:
                return [_, _dict[target - _items]]
            else:
                _dict[_items] = _


if __name__ == '__main__':
    x = input()
    x1 = int(input())
    y = x.split(',')
    x = map(lambda z: int(z), y)
    print(Solution().twoSum(list(x), x1))
