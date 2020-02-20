"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node 
in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        print( sum(self.helper(root)[1][::-1]))
    
    def helper(self, tree: TreeNode) -> set:
        if tree is None:
            return (0, [])

        left_sum = self.helper(tree.left)
        right_sum = self.helper(tree.right)

        if left_sum[0] > right_sum[0]:
            return (left_sum[0] + tree.value, left_sum[1]+[tree.val])
        return (right_sum[0] + tree.val, right_sum[1] + [tree.val])

