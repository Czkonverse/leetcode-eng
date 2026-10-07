"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

"""

import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        left = 0
        right = len(nums) - 1

        target = len(nums) - k

        while left <= right:
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            store_idx = left
            pivot = nums[right]
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]

                    store_idx += 1

            nums[right], nums[store_idx] = nums[store_idx], nums[right]

            pivot_idx = store_idx

            if pivot_idx == target:
                return nums[pivot_idx]
            elif pivot_idx < target:
                left = pivot_idx + 1
            else:
                right = pivot_idx - 1

        return -1


"""
[left, lt)       < pivot
[lt, i)          == pivot
(gt, right]      > pivot
"""

import random


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k

        left = 0
        right = len(nums) - 1

        while left <= right:
            pivot = nums[random.randint(left, right)]

            # [left, lt)       < pivot
            # [lt, i)          == pivot
            # (gt, right]      > pivot
            lt = left
            i = left
            gt = right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1

                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1

                else:
                    i += 1

            if target < lt:
                right = lt - 1

            elif target > gt:
                left = gt + 1

            else:
                return pivot

        return -1
