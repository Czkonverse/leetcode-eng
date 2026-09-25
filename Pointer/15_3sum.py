"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""

"""
First, I sort the array.

Then I iterate through the array and fix one number at index `i`. For the remaining part of the array, I use two pointers: `left = i + 1` and `right = len(nums) - 1`.

If the current sum is smaller than zero, I move `left` to the right because I need a larger value.

If the sum is larger than zero, I move `right` to the left because I need a smaller value.

If the sum equals zero, I add the triplet to the result and move both pointers inward.

To avoid duplicate triplets, I skip duplicate values for `i`, and after finding a valid triplet, I also skip duplicate values for `left` and `right`.

The time complexity is O(n²). Sorting takes O(n log n). Then, for each fixed index `i`, the two pointers scan the remaining array in O(n) time. Since the outer loop runs O(n) times, the total complexity is O(n²).

The extra space complexity is O(1), excluding the output array, because I only use a few variables such as `i`, `left`, `right`, and `total`. However, in Python, the built-in sort may use additional memory internally.

"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # sort the numbers
        nums.sort()

        res = []

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                # total = 0
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1

                    while left < right and nums[left] != nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return res
                
