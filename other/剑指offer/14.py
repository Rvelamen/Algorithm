"""
给你一根长度为n的绳子，请把绳子剪成整数长度的m段（m、n都是整数，n > 1并且m > 1），每段绳子的长度记为
k[0], k[1]...k[m - 1] 。请问k[0] * k[1] * ... * k[m - 1]
可能的最大乘积是多少？

例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3
的三段，此时得到的最大乘积是18。

"""

from functools import reduce


class Solution:
    def cuttingRope(self, n: int) -> int:
        max_sum = 0
        for _ in range(2, n + 1):
            mod = n % _
            div = n // _
            _list = [div for i in range(_ - mod)] + [div + 1 for i in range(mod)]
            max_sum = max(max_sum, reduce(lambda x, y: x * y, _list))
        return max_sum

class Solution2:
    """
    解题思路:
        n长的绳子相当于一个n的正整数
        dp[i]表示i长的绳子截断m次后的最大乘积,m>1
        状态转移：
        遍历j=1..i-1,则绳子可以分为j和i-j两部分,假设i-j也可以被分
        dp[i] = max(j*(i-j),j*dp[i-j])
        取其中最大的dp[i]

    """
    def cuttingRope(self, n: int) -> int:
        dp = [0] * (n+1)
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(dp[i-j]*j, dp[i], j*(i-j))

        return dp[n]


if __name__ == '__main__':
    print(Solution2().cuttingRope(
        2
    ))
