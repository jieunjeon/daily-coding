class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openParens = ['(', '{', '[']
        closingParens = [')', '}', ']']
        stack = []
        for char in s:
            # If we see a bracket that is part of the set 
            # of possible opening options, put it on the stack.
            if char in openParens:
                stack.append(char)
            elif char in closingParens:
                # If the stack is empty, there is an extra 
                # closing parenthesis and s is invalid.
                if len(stack) <= 0:
                    return False
                # Compares the closing parenthesis to the 
                # corresponding opening parenthesis using
                # their matching indices. We could also use
                # a hash map for this.
                if openParens.index(stack.pop()) != closingParens.index(char):
                    return False
        # If the stack is empty, the parenthesis 
        # were balanced and s is valid.
        return len(stack) == 0