"""
给定一个由整数数组 A 表示的环形数组 C，求 C 的非空子数组的最大可能和。

在此处，环形数组意味着数组的末端将会与开头相连呈环状。（形式上，当0 <= i < A.length 时 C[i] = A[i]，
且当 i >= 0 时 C[i+A.length] = C[i]）

此外，子数组最多只能包含固定缓冲区 A 中的每个元素一次。（形式上，对于子数组 C[i], C[i+1], ..., C[j]，
不存在 i <= k1, k2 <= j 其中 k1 % A.length = k2 % A.length）

 

示例 1：
输入：[1,-2,3,-2]
输出：3
解释：从子数组 [3] 得到最大和 3

示例 2：
输入：[5,-3,5]
输出：10
解释：从子数组 [5,5] 得到最大和 5 + 5 = 10

示例 3：
输入：[3,-1,2,-1]
输出：4
解释：从子数组 [2,-1,3] 得到最大和 2 + (-1) + 3 = 4

示例 4：
输入：[3,-2,2,-3]
输出：3
解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3

示例 5：
输入：[-2,-3,-1]
输出：-1
解释：从子数组 [-1] 得到最大和 -1

提示：

-30000 <= A[i] <= 30000
1 <= A.length <= 30000

"""


class Solution:
    def maxSubarraySumCircular(self, nums):
        initial_len = len(nums)
        nums = nums + nums
        _index = [0]
        dp = [nums[0]]
        if initial_len == 1:
            return nums[0]
        for i in range(1, len(nums)):
            dp.append(nums[i])
            if i % initial_len in _index:
                dp[i - 1] = dp[i - 1] - nums[i % initial_len]
            if dp[i - 1] + nums[i] >= dp[i]:
                _index.append(i)
                dp[i] = dp[i - 1] + nums[i]
            else:
                _index = [i]
        return max(dp)


class Solution2:
    def maxSubarraySumCircular(self, nums):
        initial_len = len(nums)
        nums = nums + nums
        dp = [[-10000000] * (initial_len * 2)]
        dp.append([nums[_] for _ in range(initial_len * 2)])
        for i in range(2, initial_len + 1):
            dp.append([-10000000] * (initial_len * 2))
            for j in range(0, initial_len * 2 - i):
                dp[i][j] = max(dp[i - 1][j] + nums[i - 1 + j], nums[i - 1 + j])
        res = [max(_) for _ in dp]
        return max(res)


class Solution3:
    """
    主要分两部分：首位不相接和首位相接

        1. 求区间最大和可以解决首位不相接的部分
        2. 求区间最小和然后拿sum减去区间最小和可以解决首位相接的部分。
    """

    def maxSubarraySumCircular(self, nums):
        dp = nums[:]
        dp2 = nums[:]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            dp2[i] = min(dp2[i - 1] + nums[i], nums[i])

        return max(dp) if max(dp)<0 else max(max(dp), sum(nums) - min(dp2))


class Solution4:
    """
    单区间、 双区间

    A = [0, 1, 2, 3, 4, 5, 6]是给定的循环数组，我们可以表示子段 [2, 3, 4] 为单区间 [2, 4][2,4]；
    如果我们希望表示子段 [5, 6, 0, 1]，那就是双区间 [5, 6], [0, 1][5,6],[0,1]

    T_i = A[j] + A[j+1] + A[j+2] + ... + A[A.length-1]
    R_j = max k≥j T_k
​
    ans , left + right_i+2

    若i+1则是连续的了

    """
    def maxSubarraySumCircular(self, nums):
        N = len(nums)

        ans = cur = nums[0]
        for i in nums[1:]:
            cur = i + max(cur, 0)
            ans = max(ans, cur)

        T = [None] * N
        T[-1] = nums[-1]
        for i in range(N-2, -1, -1):
            T[i] = T[i+1]+nums[i]

        R = [None] * N
        R[-1] = T[-1]
        for i in range(N-2, -1, -1):
            R[i] = max(R[i+1], T[i])

        leftsum = 0
        for i in range(N-2):
            leftsum += nums[i]
            ans = max(ans, leftsum + R[i+2])

        return ans

if __name__ == '__main__':
    print(Solution4().maxSubarraySumCircular(
        [3,-2,2,-3]
    )
    )
