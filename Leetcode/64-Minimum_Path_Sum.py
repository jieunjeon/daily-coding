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

def minPathSum(self, grid: List[List[int]]) -> int:
    """
    Brute-Force (Time Limit Exceeded)
    Time Complexity: O(2^{m+n}) since for every move, I went through 2 options: right, down
    Space Complexity: O(m+n) which is the sum of the depth m+n for the recursions
    """
    def calPathSum(grid, i, j):
        if i == len(grid) or j == len(grid[0]):
            return float('inf')
        if i == len(grid) - 1 and j == len(grid[0]) -1:
            return grid[i][j]
        return grid[i][j] + min(calPathSum(grid, i+1, j), calPathSum(grid, i, j+1))
    return calPathSum(grid, 0, 0)


def minPathSum(self, grid: List[List[int]]) -> int:
    """
    DP with extra 2d matrix
    Start by initializing all 0s in the same size of the 2d maatrix. 
    Then from the bottom right, traverse backwards and fill in the matrix with the minimum sum (from bottom / right)
    Note to be aware of the boundary conditions.

    Time Complexity: O(mn) to traverse the matrix
    Space Complexity: O(mn) to create a copy of the original matrix

    """
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