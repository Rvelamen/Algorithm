# -*- coding:utf-8 -*-
__author__: 'Rvelamen'
__data__ = '2021/10/25 22:29'

"""
240. 搜索二维矩阵 II
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

"""


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        for _index, _ in enumerate(matrix):
            if _[0] <= target <= _[-1]:
                col = self.two_search(_, target)
                if matrix[_index][col] == target:
                    return True
        return False

    def two_search(self, items, target):
        l, r = 0, len(items) - 1
        while l <= r:
            mid = (l + r) >> 1
            if items[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r


if __name__ == '__main__':
    print(Solution().searchMatrix(
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]],
        19
    ))
