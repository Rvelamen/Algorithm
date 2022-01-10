# -*- coding:utf-8 -*-
__author__: 'Rvelamen'
__data__ = '2021/10/25 23:59'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:

        def dfs(node):
            if not node:
                return None
            new_root = TreeNode(node.val)
            new_root.right = dfs(node.left)
            new_root.left = dfs(node.right)
            return new_root

        return dfs(root)


if __name__ == '__main__':
    print(Solution().mirrorTree(
        [4, 2, 7, 1, 3, 6, 9]
    ))
