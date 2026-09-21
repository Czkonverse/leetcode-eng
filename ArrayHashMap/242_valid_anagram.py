"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

"""
I use a hash map to count the frequency of each character in s. 
Then I iterate through t and decrease the corresponding count. 
If a count becomes zero, I remove that character from the hash map. 
Finally, if the hash map is empty, the two strings are anagrams.
"""
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        records = defaultdict(int)

        for ch in s:
            records[ch] += 1

        for ch in t:
            records[ch] -= 1

            if records[ch] == 0:
                del records[ch]
                
        return not records