"""
leetcode 204  https://leetcode-cn.com/problems/count-primes/
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        is_prime = [1] * n
        is_prime[0] = is_prime[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            is_prime[i*i:n:i] = [0] * ((n-1+i*i)//i + 1)
        return sum(is_prime)
