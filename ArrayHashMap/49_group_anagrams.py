"""
https://leetcode.com/problems/group-anagrams/description/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

"""
class Solution:
    def checkAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False

        s_dict = {}

        for ch in s:
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1

        for ch in t:
            if ch in s_dict:
                s_dict[ch] -= 1
            else:
                return False

            if s_dict[ch] == 0:
                del s_dict[ch]

        return not s_dict

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pass

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]

    solution = Solution()

    res = solution.groupAnagrams(strs)
    print(res)