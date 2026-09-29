"""
739. Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

"""
My first approach is the brute-force solution.

For each day, I scan the following days and find the first day with a higher temperature. If I find one, I store the difference between the two indices. Otherwise, I store zero.

The time complexity is O(n²) because for each day, I may need to scan all the remaining days in the worst case.

The space complexity is O(n) because I use an output array to store the result. If we exclude the output array, the extra space is O(1).
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        res = []
        for left in range(len(temperatures)):
            today = temperatures[left]
            found = False
            for right in range(left + 1, len(temperatures)):
                if temperatures[right] > today:
                    res.append(right - left)
                    found = True
                    break

            if not found:
                res.append(0)

        return res


"""
To optimize it, I use a monotonic decreasing stack.

The stack stores the indices of days that are still waiting for a warmer temperature. 
While the current temperature is higher than the temperature at the top of the stack, I pop that index and calculate the waiting time as the difference between the current index and the previous index.

Then I push the current index onto the stack.

The time complexity is O(n) because each index is pushed onto the stack once and popped at most once.

The space complexity is O(n) because, in the worst case, the stack may contain all indices. The output array also takes O(n) space.
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)

        answer = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()

                answer[prev_index] = i - prev_index

            stack.append(i)

        return answer
