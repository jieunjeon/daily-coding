"""
https://leetcode.com/problems/broken-calculator/

991. Broken Calculator

On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.
"""

class Solution(object):
    def brokenCalc(self, X, Y):
        """
        :type X: int
        :type Y: int
        :rtype: int
        """
        res = 0
        while X < Y:
            if Y % 2 == 0:
                Y = Y / 2
            else:
                Y += 1
            res += 1
        if X > Y:
            res += X - Y
        return res
        

"""
Instead of working from x -> y, we could work backwards instead and work from y -> x.
If y is divisible by 2, divide by 2. Otherwise add 1. (greedily)
If x >= y, terminate the loop, and add the difference of x-y, since x -> y only allows
to subtract by 1.

"""