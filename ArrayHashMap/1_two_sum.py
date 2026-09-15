"""
https://leetcode.com/problems/two-sum/description/
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List

"""
My first thought is to use a brute-force approach. I can iterate through the array and, for each number, search for its complement in the remaining part of the array.
However, this requires O(n²) time. 
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):

            complement = target - nums[i]
            for j in range(i + 1, len(nums)):
                if complement == nums[j]:
                    return [i, j]

        return []
                


"""
But we can improve this by using a hash map. While iterating the array, I store previously seen numbers and their indices. 
For each number, I calculate its complement and check whether it already exists in the hash map. If it does, I return the two indices.
This reduces the time complexity from O(n²) to O(n), at the cost of O(n) extra space.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        comp_dict = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in comp_dict:
                return [idx, comp_dict[complement]]

            comp_dict[num] = idx

        return []

