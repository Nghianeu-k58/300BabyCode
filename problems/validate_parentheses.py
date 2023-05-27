"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:

    @staticmethod
    def validate_parentheses(s):
        """Handling parentheses."""
        stack = []
        parentheses = {
            "]": "[",
            ")": "(",
            "}": "{"
        }
        for element in s:
            if element in parentheses:
                if stack and (stack[-1] == parentheses[element]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)
        return False if stack else True
