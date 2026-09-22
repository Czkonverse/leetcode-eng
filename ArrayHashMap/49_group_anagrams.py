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

"""
My first idea is to use a hash map.

I iterate through each string in the array and sort its characters. Anagrams have the same sorted representation. For example, "eat", "tea", and "ate" all become "aet" after sorting.

So I can use the sorted string as the key in the hash map and store all strings with the same key in a list.

For each string, I generate its sorted representation and append the original string to the corresponding group.

Finally, I return all the groups stored in the hash map.

Let n be the number of strings and k be the maximum length of a string.

Sorting one string takes O(k log k) time. Since there are n strings, the total time complexity is:

O(n × k log k)

The space complexity is O(n × k) in the worst case, because the hash map may store a different sorted key for each string.
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)

        return list(ans.values())

"""
My second idea is to avoid sorting by using character frequencies as the key.

Since each string contains only lowercase English letters, I can create an array of size 26 to count the frequency of each character.

For each character, I calculate its index using:

ord(c) - ord('a')

and increment the corresponding count.

Two anagrams must have exactly the same character frequencies, so they will produce the same frequency vector.

Therefore, I can use this frequency vector as the key in the hash map and group all strings with the same frequency pattern together.

However, a Python list cannot be used as a dictionary key because lists are mutable and unhashable. So I convert the frequency array into a tuple before using it as the key.

Let n be the number of strings and k be the maximum length of a string.

For each string, I iterate through all of its characters once, so processing one string takes O(k) time. Since there are n strings, the total time complexity is:

O(n × k)

The frequency array has a fixed size of 26, so it takes O(1) space. The hash map can contain up to n different keys, so the auxiliary space complexity is O(n).

"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        ans = defaultdict(list)

        # multi-hot encoding
        for s in strs:

            multi_encode = [0] * 26
            for c in s:
                multi_encode[ord(c) - ord("a")] += 1

            ans[tuple(multi_encode)].append(s)

        return list(ans.values())


"""
Why do you convert the list into a tuple?

Because dictionary keys must be hashable. A list is mutable and unhashable, while a tuple is immutable and can be used as a dictionary key.
"""