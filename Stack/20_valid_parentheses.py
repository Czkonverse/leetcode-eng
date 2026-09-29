"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Example 5:
Input: s = "([)]"
Output: false

"""

"""
I would use a stack because the most recently opened bracket must be closed first, which follows the LIFO principle.

I iterate through the string. If I see an opening bracket, I push it onto the stack. If I see a closing bracket, I first check whether the stack is empty. If it is, the string is invalid.

Otherwise, I pop the top element and check whether it matches the current closing bracket. If they do not match, I return false.

After processing the entire string, the stack must be empty. Otherwise, there are unmatched opening brackets.

The time complexity is O(n) because I scan the string once, and each push and pop operation is O(1).

The space complexity is O(n) in the worst case, when all characters are opening brackets.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {"}": "{", ")": "(", "]": "["}
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False

                if mappings[char] != stack.pop():
                    return False

        return not stack
