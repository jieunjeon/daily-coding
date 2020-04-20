"""
https://leetcode.com/problems/valid-parenthesis-string/


Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        if str == "":
            return True
        
        openStack = []
        starStack = []
        length = len(s)
        
        for i in range(len(s)):
            if s[i] == '(':
                openStack.append(i)
            elif s[i] == '*':
                starStack.append(i)
            else:
                if openStack != []:
                    openStack.pop()
                elif starStack != []:
                    starStack.pop()
                else:
                    return False
        
        while openStack != []:
            if starStack == []:
                return False
            elif openStack[len(openStack)-1] < starStack[len(starStack)-1]:
                openStack.pop()
                starStack.pop()
            else:
                return False
        
        return True