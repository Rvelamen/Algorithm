"""
重建二叉树

示例 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

示例 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]

# Definition for a binary tree node.


"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        # preorder = [3,9,20,15,7]
        # inorder = [9,3,15,20,7]
        def build_child_tree(pre_sub, in_sub):
            if not pre_sub or not in_sub:
                return None

            temp = TreeNode(pre_sub[0])
            if len(pre_sub) == 1:
                return temp
            mid_index = in_sub.index(pre_sub[0])
            temp.left = build_child_tree(pre_sub[1:mid_index + 1], in_sub[0:mid_index])
            temp.right = build_child_tree(pre_sub[mid_index + 1:], in_sub[mid_index + 1:])

            return temp

        return build_child_tree(preorder, inorder)


class Solution2:
    def buildTree(self, preorder, inorder):
        def build_child_tree(l, r, ll):
            if l > r:
                return None
            temp = TreeNode(preorder[l])
            if l == r:
                return temp

            mid_index = _index[temp.val]
            temp.left = build_child_tree(l+1, l+mid_index-ll, ll)
            temp.right = build_child_tree(l+mid_index-ll+1, r,   mid_index+1)

            return temp

        _index = {_: _index for _index, _ in enumerate(inorder)}
        return build_child_tree(0, len(inorder) - 1, 0)


if __name__ == '__main__':
    print(Solution2().buildTree([1, 2, 3],
                               [1, 2, 3]))
