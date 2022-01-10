"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1

"""

class Solution:
    def movingCount(self, m, n, k) -> int:
        def cal_pos(i, j):
            temp = str(i) + str(j)
            return sum([int(_) for _ in temp]) <= k

        mov_pos = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def bfs():
            flag = [[None]*n for _ in range(m)]
            queue = [(0, 0)]
            sum = 0
            flag[0][0] = True

            while queue:
                temp = queue.pop(0)
                sum += 1
                for pos in mov_pos:
                    x_index = temp[0] + pos[0]
                    y_index = temp[1] + pos[1]


                    if x_index >= 0 and y_index >= 0 and x_index < m and y_index < n and not flag[x_index][y_index] and cal_pos(x_index, y_index):
                        flag[x_index][y_index] = True
                        queue.append((x_index, y_index))

            return sum

        return bfs()


if __name__ == '__main__':
    print(Solution().movingCount(
        3,1,0
    ))
