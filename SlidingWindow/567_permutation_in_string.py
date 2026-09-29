"""
567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

"""
Approach 1: Sorting + Fixed-Size Sliding Window

My first approach is to use a fixed-size sliding window.

The window size is equal to the length of s1. I first sort s1, then slide the window through s2. For each window, I sort the substring and compare it with the sorted s1.

If they are equal, the window is a permutation of s1, so I return true.

Let n be the length of s2 and m be the length of s1.
The time complexity is O(n × m log m) because there are about n windows, and sorting each window takes O(m log m).
The space complexity is O(m) because sorting creates temporary strings of length m.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        s1_sort = "".join(sorted(s1))

        left = 0
        right = left + window_size
        while right <= len(s2):
            subarray = s2[left:right]
            subarray_sort = "".join(sorted(subarray))

            if s1_sort == subarray_sort:
                return True
            else:
                left += 1
                right = left + window_size

        return False


"""
Approach 2: Frequency Array + Sliding Window

We can optimize the first approach by avoiding sorting.

Since the strings contain only lowercase English letters, I use two arrays of size 26 to store character frequencies: one for s1 and one for the current window in s2.

When the window moves, I add the new character on the right and remove the character that leaves from the left. Then I compare the two frequency arrays.

If they are equal, the current window is a permutation of s1.

The time complexity is O(n) because each character is added to and removed from the sliding window at most once, and comparing two arrays of size 26 is constant time.

The space complexity is O(1) because both frequency arrays have a fixed size of 26.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        window_size = len(s1)

        s1_count = [0] * 26
        window_count = [0] * 26

        # first time to build the s1_count and window_count
        for i in range(window_size):
            s1_count[ord(s1[i]) - ord("a")] += 1
            window_count[ord(s2[i]) - ord("a")] += 1

        if s1_count == window_count:
            return True

        # iterate throught the remaining part of the s2
        for right in range(window_size, len(s2)):
            window_count[ord(s2[right]) - ord("a")] += 1

            left = right - window_size
            window_count[ord(s2[left]) - ord("a")] -= 1

            if s1_count == window_count:
                return True

        return False
