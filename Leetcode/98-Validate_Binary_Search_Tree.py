# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root) :
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))
    
    def isValidBSTHelper(self, n, low, high):
        if not n:
            return True
        if ((n.val > low and n.val < high) and
            self.isValidBSTHelper(n.left, low, n.val) and
            self.isValidBSTHelper(n.right, n.val, high)):
            return True
        return False