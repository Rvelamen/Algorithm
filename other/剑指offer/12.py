"""

给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false


"""

class Solution:
    def exist(self, board, word) -> bool:
        row = len(board)
        col = len(board[0])
        begin_position = []

        for i, item in enumerate(board):
            for j, item2 in enumerate(item):
                if item2 == word[0]:
                    begin_position.append((i, j))

        print(begin_position)
        # 左上右下
        move_pos = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for _ in begin_position:
            flag = [[None] * col for _ in range(row)]
            queue = []

            queue.append((_[0], _[1], 1))
            flag[_[0]][_[1]] = True

            while queue:
                temp = queue.pop(0)
                print(temp)
                print(flag)

                if temp[2] == len(word) and board[temp[0]][temp[1]] == word[-1]:
                    return True

                for al in move_pos:
                    x_index = temp[0] + al[0]
                    y_index = temp[1] + al[1]

                    if x_index >= 0 and x_index < row and y_index >= 0 and y_index < col and not flag[x_index][
                        y_index] and board[x_index][y_index] == word[temp[2]]:
                        print(x_index, y_index)
                        queue.append((x_index, y_index, temp[2] + 1))
                        flag[x_index][y_index] = True
        return False


class Solution2(object):
    def exist(self, board, word) -> bool:
        row = len(board)
        col = len(board[0])
        begin_position = []

        for i, item in enumerate(board):
            for j, item2 in enumerate(item):
                if item2 == word[0]:
                    begin_position.append((i, j))

        res = False
        # 左上右下
        move_pos = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        def DFS(i, j, count):
            res = False
            if count == len(word) and board[i][j] == word[-1]:
                return True

            for al in move_pos:
                x_index = i + al[0]
                y_index = j + al[1]

                if x_index >= 0 and x_index < row and y_index >= 0 and y_index < col and not flag[x_index][y_index] and board[x_index][y_index] == word[count]:
                    flag[x_index][y_index] = True
                    res = DFS(x_index, y_index, count + 1)
                    if res:
                        return True
                    flag[x_index][y_index] = False

            return res

        for _ in begin_position:
            flag = [[None] * col for _ in range(row)]
            flag[_[0]][_[1]] = True
            if DFS(_[0], _[1], 1):
                return True
        return False



if __name__ == '__main__':
    # print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
    # print(Solution().exist([["a", "b"], ["c", "d"]], "abcd"))
    # print(Solution2().exist([["a", "b"], ["c", "d"]], "abcd"))
    # print(Solution2().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
    # print(Solution2().exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"))
    print(Solution2().exist(
        [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]],
        "AAB"
    ))