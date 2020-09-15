#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     def __init__(self):
#         self.res = []

#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         self.PreOrder(p)
#         p_list = self.res
#         self.res =[]
#         self.PreOrder(q)
#         return self.res == p_list

#     def PreOrder(self, root):
#         if not root:
#             self.res.append('null')
#             return
          # 如果用先序遍历会发生错误
#         self.res.append(root.val)
#         self.PreOrder(root.left)
#         self.PreOrder(root.right)

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
# @lc code=end
