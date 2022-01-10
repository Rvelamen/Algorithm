"""
1167. 连接棒材的最低费用
为了装修新房，你需要加工一些长度为正整数的棒材 。棒材以数组 sticks 的形式给出，其中 sticks[i] 是第 i 根棒材的长度。

如果要将长度分别为 x 和 y 的两根棒材连接在一起，你需要支付 x + y 的费用。 由于施工需要，你必须将所有棒材连接成一根。

返回你把所有棒材 sticks 连成一根所需要的最低费用。注意你可以任意选择棒材连接的顺序。



示例 1：

输入：sticks = [2,4,3]
输出：14
解释：从 sticks = [2,4,3] 开始。
1. 连接 2 和 3 ，费用为 2 + 3 = 5 。现在 sticks = [5,4]
2. 连接 5 和 4 ，费用为 5 + 4 = 9 。现在 sticks = [9]
所有棒材已经连成一根，总费用 5 + 9 = 14

"""
from sortedcontainers import SortedList

class Solution:
    def connectSticks(self, sticks) -> int:
        new_num = SortedList(sticks)
        num_sum = 0
        while len(new_num) > 1:
            x = new_num.pop(0)
            y = new_num.pop(0)
            num_sum += x + y
            new_num.add(x+y)
        return num_sum


if __name__ == '__main__':
    print(Solution().connectSticks(
        [2, 4, 3]
    ))