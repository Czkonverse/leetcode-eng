"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""

"""
My first approach is brute force.

I use two nested loops to check every possible pair of lines.

For each pair, the width is `j - i`, and the height is limited by the shorter line, so the area is:

`(j - i) * min(height[i], height[j])`

I calculate the area for every pair and keep track of the maximum.

The time complexity is O(n²), because I check all pairs of lines using two nested loops.

The space complexity is O(1), because I only use a few extra variables and do not use any additional data structure.

"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                width = j - i
                height_min = min(height[i], height[j])

                area = width * height_min

                max_area = max(max_area, area)

        return max_area
    

"""
A better approach is to use two pointers.

I start with one pointer at the beginning and the other at the end, so the initial width is the maximum possible.

For each pair, I calculate the area as:

`(right - left) * min(height[left], height[right])`

Then I update the maximum area.

After that, I move the pointer at the shorter line.

The reason is that the width always becomes smaller after moving a pointer. So if I want to get a larger area, I need a chance to find a taller line. Since the shorter line is the limiting factor, I move that side.

I continue until the two pointers meet.

The time complexity is O(n), because each pointer only moves in one direction and moves at most n times in total.

The space complexity is O(1), because I only use a few extra variables such as `left`, `right`, and `max_area`.

"""
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            width = right - left
            height_min = min(height[left], height[right])
            area = width * height_min

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area