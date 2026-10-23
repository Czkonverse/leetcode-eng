"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

"""
### 1. Approach — Dynamic Programming

My first approach is to use Dynamic Programming.

For each house, I have two choices: either rob the current house or skip it.

If I rob the current house, I cannot rob the previous house, so the total amount is the money in the current house plus the maximum amount from two houses before.

If I skip the current house, the maximum amount remains the same as the previous house.

So, the recurrence relation is:

`dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])`

Here, `dp[i]` represents the maximum amount of money I can rob from the first `i + 1` houses.

For the base cases:

- `dp[0] = nums[0]`
- `dp[1] = max(nums[0], nums[1])`

Then, I iterate through the remaining houses and update the DP array.

Finally, I return `dp[-1]`.

**Time Complexity:** O(n), because I traverse the array once.

**Space Complexity:** O(n), because I use an additional DP array.
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]


"""

### 2. Optimization — Constant Space

We can optimize the space complexity.

Since each state only depends on the previous two states, we don't need to store the entire DP array.

Instead, I use two variables to keep track of the previous two results.

For each house, I calculate the maximum amount by either robbing the current house or skipping it.

Then, I update the two variables and move to the next house.

Finally, I return the latest result.

**Time Complexity:** O(n), because I still traverse the array once.

**Space Complexity:** O(1), because I only use a constant amount of extra space.

This is the optimized solution.
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0, 0]

        for i in range(len(nums)):
            current = max(dp[0] + nums[i], dp[1])

            dp[0], dp[1] = dp[1], current

        return dp[1]
