class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = [-1 for _ in range(len(nums))]
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            res = max(self.dfs(nums, i, dp), res)
        return res

    def dfs(self, nums, i, dp):
        if dp[i] != -1:
            return dp[i]
        a = 1
        for j in range(0, i):
            if nums[j] < nums[i]:
                a = max(a, self.dfs(nums, j, dp)+1)
        dp[i] = a
        return a

enum

x = Solution()
print(x.lengthOfLIS([4, 10, 4, 3, 8, 9]))
