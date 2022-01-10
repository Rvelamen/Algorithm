"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k: int) -> int:
        inorder = []
        new_tree = TreeNode(root[0])

        # 层次遍历还原树
        queue = []
        temp = new_tree
        for i in root[1:]:
            treeNode = TreeNode(i)
            if temp.left and temp.right:
                temp = queue.pop(0)

            if not temp.left:
                temp.left = treeNode
                queue.append(treeNode)
            elif not temp.right:
                temp.right = treeNode
                queue.append(treeNode)

        # 中序遍历
        def DFS(tree):
            if not tree:
                return
            DFS(tree.left)
            inorder.append(tree.val)
            DFS(tree.right)

        DFS(new_tree)
        print(inorder)
        return inorder[k-1]


if __name__ == '__main__':
    print(Solution().kthSmallest(
        [3, 1, 4, None, 2],
        1
    ))
