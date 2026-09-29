"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

"""
1. Standard Binary Search

“I use binary search on the sorted array. I compare the middle element with the target. If they are equal, I return the index. If the middle value is larger, I search the left half; otherwise, I search the right half.

The time complexity is O(log n) because the search space is halved in each iteration, and the space complexity is O(1).”
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


"""
2. Lower Bound

“Lower bound finds the first index where the value is greater than or equal to the target.

When nums[mid] >= target, the current index is a possible answer, but I continue searching to the left for an earlier position.

The time complexity is O(log n), and the space complexity is O(1).”
"""


class Solution:
    def lower_bound(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        ans = len(nums)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:  # important
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


"""
3. Upper Bound

“Upper bound finds the first index where the value is strictly greater than the target.

When nums[mid] > target, the current index is a possible answer, but I continue searching to the left for an earlier position.

The time complexity is O(log n), and the space complexity is O(1).”
"""


class Solution:
    def upper_bound(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        ans = len(nums)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:  # important
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


"""
普通：== target
lower：>= target
upper：> target
"""
