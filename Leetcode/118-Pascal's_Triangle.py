"""
https://leetcode.com/problems/pascals-triangle/

Pascal's Triangle is a triangle where all numbers are the sum of the two numbers above it. Here's an example of the Pascal's Triangle of size 5.
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an integer n, generate the n-th row of the Pascal's Triangle.

"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1] * i for i in range(1, numRows + 1)]

        for i in range(numRows):
            for j in range(1, i):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        return triangle
        
"""
We can build out the Pascal's Triangle by starting from the first row, and then build the second row etc. until we reach the n-th row as following by the triangle as a 2D list.

"""