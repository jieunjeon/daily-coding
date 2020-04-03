"""
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

class Solution(object):
    def getReady(self, num):
        seen = []
        while num > 9:
            seen.append(num%10)
            num = num//10
        seen.append(num)
        return seen
    def isHappy(self, n):
        """
        :type n: intå
        :rtype: bool
        """
        seen = self.getReady(n)
        res = 0
        previousList = []
        
        while res not in previousList:
            for i in seen:
                res += i*i
        
            if res in previousList:
                return False
            if res == 1:
                return True
            previousList.append(res)
            seen = self.getReady(res)
            res = 0
            
        