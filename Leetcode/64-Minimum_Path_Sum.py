"""
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""

class Solution:
    # DP
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        h = len(grid)
        w = len(grid[0])
        dp = [x[:] for x in [[0] * w] * h]
        
        for row in range(h):
            for col in range(w):
                if row == 0 and col == 0:
                    dp[row][col] = grid[row][col]
                else:
                    pos1 = float('inf')
                    pos2 = float('inf')
                    if row != 0:
                        pos1 = dp[row-1][col]
                    if col != 0:
                        pos2 = dp[row][col-1]
                    dp[row][col] = grid[row][col] + min(pos1, pos2)

        return dp[h-1][w-1]
