class Solution:
    def isValid(self, s: str) -> bool:
        #what i solved by my own
        from collections import deque

        left = deque()
        right = 0

        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                left.append(ch)
            elif ch == ")" and left:
                if left.pop() == "(":
                    continue
                else:
                    return 0
            elif ch == "}" and left:
                if left.pop() == "{":
                    continue
                else:
                    return 0
            elif ch == "]" and left:
                if left.pop() == "[":
                    continue
                else:
                    return 0
            else:
                right += 1

        if len(left) == 0 and right == 0:
            return 1
        else:
            return 0

"""
#some cool solution from internet
class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
"""
