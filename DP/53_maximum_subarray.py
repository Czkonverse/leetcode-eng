"""
53. Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

"""
My first idea is to use brute force.

I can enumerate all possible subarrays with two loops, calculate the sum of each subarray, and keep track of the maximum sum. 
Since there are O(n²) subarrays and calculating each sum takes O(n), the total time complexity is O(n³).

Then I can optimize it with dynamic programming.
I define `dp[i]` as the maximum subarray sum ending at index `i`. 
At each position, I either start a new subarray from `nums[i]`, or extend the previous subarray.
So the transition is:
`dp[i] = max(nums[i], dp[i - 1] + nums[i])`
This gives O(n) time and O(n) space.

Finally, since `dp[i]` only depends on `dp[i - 1]`, I can replace the DP array with one variable, `current_sum`, and use another variable, `max_sum`, to track the global maximum.
So the final solution runs in O(n) time and O(1) space.
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_sum = nums[0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):  # mistake point
                subarray = nums[i:j]  # mistake point
                sum_temp = sum(subarray)

                if sum_temp > max_sum:
                    max_sum = sum_temp

        return max_sum


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp = [0] * len(nums)

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        max_sum = nums[0]

        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])

            max_sum = max(max_sum, current_sum)

        return max_sum
