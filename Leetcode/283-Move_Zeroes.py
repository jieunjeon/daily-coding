"""
https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeroIndex = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:

                nums[i],nums[zeroIndex] = nums[zeroIndex],nums[i]
                zeroIndex += 1

   def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 
        
        for i in range(0,nums.count(0)):
            nums.remove(0)
            nums.append(0)
                    