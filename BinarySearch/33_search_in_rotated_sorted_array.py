"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
"""

"""
当前搜索范围：
[left, right]
两边都包含
→ while left <= right

mid 已经单独检查过
→ 后面不需要再包含 mid

左边区间：
[left, mid)
→ <= target <

右边区间：
(mid, right]
→ < target <=
"""

"""
I use binary search because the array is still partially sorted after rotation.

At each step, one side of the array must be sorted. I first identify the sorted half, then check whether the target lies inside that range. 
Based on that, I discard the other half and continue the search.

The time complexity is O(log n) because I reduce the search space by half each time.
The space complexity is O(1) because I only use a few pointers.

"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
