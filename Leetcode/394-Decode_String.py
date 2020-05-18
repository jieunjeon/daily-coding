"""
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""

class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        i = 0
        while i < len(s):
            if s[i].isalpha():
                res += s[i]
                i += 1
                continue

            if s[i].isdigit():
            # get the number
                num = 0
                while s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                # parse string in bracket
                bracket = 1
                i += 1
                innerstr = ""
                while bracket > 0:
                    if s[i] == '[':
                        bracket += 1
                    if s[i] == ']':
                        bracket -= 1
                    innerstr += s[i]
                    i += 1
                res = res + num * self.decodeString(innerstr[:-1])

            return res