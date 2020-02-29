"""
https://leetcode.com/problems/valid-palindrome-ii/
680. Valid Palindrome 2

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        count = 0
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                count += 1
                
                # If two pairs are not equal return False
                if count >= 2:
                    return False
                
                # If one pair not equal, delete left and right
                a1 = s[0:i] + s[i+1:]
                a2 = s[0:len(s) - 1 - i] + s[len(s) - 1 - i + 1:]

                # Check if one of them would be palindrome, that'd be OK
                if a1 == a1[::-1] or a2 == a2[::-1]:
                    return True

        # Otherwise return False
        return False