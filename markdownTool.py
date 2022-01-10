class Solution:
    def getLongestPalindrome(self, A: str) -> int:
        if len(A) < 2:
            return 1

        dp = [[False] * len(A) for _ in A]

        ans = 0
        for _len in range(len(A)):
            for i in range(len(A) - _len):
                j = i + _len

                if A[i] == A[j]:
                    if _len <= 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j]:
                        ans = _len + 1
        return ans