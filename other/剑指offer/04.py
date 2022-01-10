"""
剑指 Offer 04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


class Solution:
    def findNumberIn2DArray(self, matrix, target) -> bool:
        if not matrix:
            return False
        for i in range(len(matrix)):
            if not matrix[i]:
                return False
            if matrix[i][0] <= target <= matrix[i][-1]:
                col = self.two_search(matrix[i], target)
                if matrix[i][col] == target:
                    return True
        return False

    def two_search(self, m_list, target):
        if not m_list:
            return -1
        higth = len(m_list)
        low = 0
        while higth > low:
            mid = (higth + low) // 2
            if m_list[mid] == target:
                low = mid + 1
            elif m_list[mid] > target:
                higth = mid
            elif m_list[mid] < target:
                low = mid + 1
        return low - 1


if __name__ == '__main__':
    print(Solution().findNumberIn2DArray(
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
        , 19))
