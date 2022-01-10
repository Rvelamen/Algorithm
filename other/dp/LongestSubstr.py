class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
