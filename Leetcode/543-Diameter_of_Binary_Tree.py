"""
https://leetcode.com/problems/diameter-of-binary-tree/
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        return self.dfs(root)
        
    def dfs(self, root):
        if root == None:
            return 0
        if root.left== None and root.right == None:
            return 1
        tmp = 1
        if root.left != None:
            tmp += self.dfs(root.left) 
        if root.right != None:
            tmp += self.dfs(root.right) 
        return tmp
    

            