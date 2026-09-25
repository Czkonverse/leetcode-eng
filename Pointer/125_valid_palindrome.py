"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
 
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""


"""
My first approach is to build a cleaned string.
I keep only letters and digits, convert all letters to lowercase, and then compare the string with its reverse.
This approach takes O(n) time and O(n) extra space.
"""

class Solution:
    def is_alphanumeric(self, c):
        return (
            'a' <= c <= 'z'
            or 'A' <= c <= 'Z'
            or '0' <= c <= '9'
        )

    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if self.is_alphanumeric(char))

        return s == s[::-1]

"""
My second approach uses two pointers.

I place one pointer at the beginning and one at the end. I skip all non-alphanumeric characters, then compare the two characters after converting them to lowercase.

If they are different, I return false. Otherwise, I move both pointers toward the center.

This approach also takes O(n) time, but only O(1) extra space.
"""
class Solution:
    def is_alphanumeric(self, c):
        return (
            'a' <= c <= 'z'
            or 'A' <= c <= 'Z'
            or '0' <= c <= '9'
        )

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.is_alphanumeric(s[left]):
                left += 1

            while left < right and not self.is_alphanumeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True