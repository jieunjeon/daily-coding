"""
https://leetcode.com/problems/valid-palindrome/
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


"""

class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1  
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower(): 
                    return False
                else:
                    left += 1
                    right -= 1
            elif not s[left].isalnum():  # left is not a alphanumeric, then move left
                left += 1
            else:  # right is not a alphanumeric, then move right
                right -= 1
        return True