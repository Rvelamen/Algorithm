import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        res = math.log(n, 2)
        if n == 1:
            return True
        return True if round(res, 8) == int(res) and int(math.pow(2, int(res))) == n and n % 2 == 0 else False

if __name__ == '__main__':
    print(Solution().isPowerOfTwo(536870913))
    print(Solution().isPowerOfTwo(
536870912))