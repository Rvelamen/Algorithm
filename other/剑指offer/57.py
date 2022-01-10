# -*- coding:utf-8 -*-
__author__: 'Rvelamen'
__data__ = '2021/10/29 8:37'

"""
剑指 Offer 57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：
1 <= target <= 10^5
"""


class Solution:
    def findContinuousSequence(self, target: int):
        l, r = 1, 2
        res = []
        res_sum = l
        while l <= target:
            if res_sum + r == target:
                res.append([_ for _ in range(l, r + 1)])
                res_sum += r
                r += 1
            if res_sum + r < target:
                res_sum += r
                r += 1
            else:
                res_sum -= l
                l += 1
        return res


if __name__ == '__main__':
    print(Solution().findContinuousSequence(
        100
    ))
