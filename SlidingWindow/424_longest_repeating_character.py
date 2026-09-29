"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.


Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                record = defaultdict(int)
                subarray = s[i : j + 1]

                for char in subarray:
                    record[char] += 1

                window_len = j - i + 1
                max_freq = max(record.values())

                replacements = window_len - max_freq

                if replacements <= k:
                    max_len = max(max_len, window_len)

        return max_len


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0

        record = defaultdict(int)

        max_len = 0
        max_freq = 0
        for right in range(len(s)):
            record[s[right]] += 1

            max_freq = max(record.values())

            while (right + 1 - left) - max_freq > k:
                record[s[left]] -= 1
                left += 1

                max_freq = max(record.values())

            max_len = max(max_len, right + 1 - left)

        return max_len
