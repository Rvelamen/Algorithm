# -*- coding:utf-8 -*-
__author__: 'Rvelamen'
__data__ = '2021/10/27 8:40'

"""
496. 下一个更大元素 I
给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。

请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

 

示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
    
"""


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        _map = {_: _index for _index, _ in enumerate(nums2)}
        _len = len(nums2)
        res = []
        for _ in nums1:
            if _map[_] == _len-1:
                res.append(-1)
                continue
            temp = -1
            for __ in nums2[_map[_] + 1: ]:
                if __ > _:
                    temp = __
                    break
            res.append(temp)
        return res

if __name__ == '__main__':
    print(Solution().nextGreaterElement(
        [4, 1, 2],
        [1, 3, 4, 2]
    ))
