"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
容易犯错的地方，如何遍历所有的子串？
"""

"""
Approach 1 — Brute Force

My first approach is brute force.

I enumerate all possible substrings. For each substring, I use a set to check whether it contains duplicate characters. If it has no duplicates, I update the maximum length.

The time complexity is O(n³) in the worst case, because there are O(n²) substrings, and checking each substring can take O(n) time.

The space complexity is O(n) for the set used to check duplicates.
"""
from collections import defaultdict


class Solution:
    def ckeck_duplicate(self, s):
        record = set()
        for char in s:
            if char in record:
                return False
            else:
                record.add(char)
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        lengths = []
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                subarray = s[i:j]
                if self.ckeck_duplicate(subarray):
                    lengths.append(len(subarray))

        return max(lengths)


"""
Approach 2 — Sliding Window with a Set

We can optimize this using a sliding window.

I use two pointers, left and right, and a set to store the characters in the current window.

The right pointer expands the window. If s[right] already exists in the set, I move left forward and remove characters until there is no duplicate.

Then I update the maximum window length.

The time complexity is O(n) because each character is added to and removed from the set at most once.

The space complexity is O(n) in the worst case.

Approach 3 — Sliding Window with Last Seen Positions

We can further optimize how we move the left pointer by storing the last index of each character in a hash map.

When I see a duplicate character that is still inside the current window, I can move left directly to one position after its previous index.

The condition last_seen[char] >= left is important because an earlier occurrence may already be outside the current window. We should never move left backward.

The time complexity is O(n) because we scan the string only once.

The space complexity is O(n) in the worst case.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = set()

        max_len = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1

            window.add(s[right])

            max_len = max(max_len, right + 1 - left)

        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        last_seen = defaultdict(int)

        max_len = 0

        for right in range(len(s)):
            char = s[right]

            if (
                char in last_seen and last_seen[char] >= left
            ):  # mistake point, why - abba
                left = last_seen[char] + 1

            last_seen[char] = right

            max_len = max(max_len, right + 1 - left)

        return max_len
