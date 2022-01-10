"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

"""


class Solution:
    def maxProduct(self, nums):
        dpmax = [nums[0]]
        dpmin = [nums[0]]
        for i in range(1, len(nums)):
            dpmax.append(nums[i])
            dpmin.append(nums[i])
            dpmax[i] = max(dpmax[i - 1] * nums[i], dpmin[i - 1] * nums[i], dpmax[i])
            dpmin[i] = min(dpmax[i - 1] * nums[i], dpmin[i - 1] * nums[i], dpmin[i])
        return max(dpmin + dpmax)


if __name__ == '__main__':
    print(Solution().maxProduct([-2, 0, -1]))
