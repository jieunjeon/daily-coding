"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        strCounter = Counter(s)
        
        for i, v in strCounter.items():
            if v == 1:
                return s.find(i)
        
        return -1