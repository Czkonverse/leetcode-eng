"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

"""

"""
My first thought is to use a brute-force approach. 
For each element, I could search the remaining part of the array for the same value, but this would take O(n²) time.
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

"""
We can improve this by using a set to keep track of the elements we have already seen. 
While iterating through the array, if the current element is already in the set, we have found a duplicate and can return true immediately. 
Otherwise, we add it to the set.
This gives us O(n) time complexity and O(n) space complexity.
"""
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        records = set()

        for i in range(len(nums)):
            if nums[i] in records:
                return True
            records.add(nums[i])

        return False