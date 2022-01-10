# -*- coding:utf-8 -*-
__author__: 'Rvelamen'
__data__ = '2021/10/27 12:58'

"""
剑指 Offer 54. 二叉搜索树的第k大节点
给定一棵二叉搜索树，请找出其中第k大的节点。

 

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4


"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

class Solution:
    def kthLargest(self, root, k):
        pass