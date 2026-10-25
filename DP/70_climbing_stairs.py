"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

"""
If we want to reach the fifth stair, I can come from either the fourth stair or the third stair because I can climb either one or two steps at a time.

Therefore, the number of ways to reach the current stair depends on the number of ways to reach the previous two stairs.
This is a typical Dynamic Programming problem.

We can derive the recurrence relation(state transition equation):

dp[n] = dp[n - 1] + dp[n - 2]
dp[n] represents the number of ways to reach the nth stair.

Next, we need to consider the base cases.
When n = 0, there is only one way: do nothing.
When n = 1, there is also only one way: climb one step.

Therefore, we initialize dp[0] = dp[1] = 1.
Then, we iterate from 2 to n, calculating the number of ways to reach each stair.
Finally, the result is stored in dp[n].

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


"""
We don't need to store the entire DP array because each state depends only on the previous two states.
Instead, we can use two variables, previous_one and previous_two, both initialized to 1.

In each iteration, we calculate the current state and update these two variables.

This reduces the space complexity from O(n) to O(1), while the time complexity remains O(n).

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1

        previous_one = 1
        previous_two = 1

        for _ in range(2, n + 1):
            current = previous_one + previous_two

            previous_two = previous_one
            previous_one = current

        return previous_one
