"""
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
"""

"""
My approach is to use Depth-First Search (DFS) to calculate the area of each island recursively.

For each land cell, we explore its four neighboring directions: up, down, left, and right.

We first handle the base cases. If the current cell is out of bounds or is water, we return zero.
Otherwise, we count the current cell as one unit of area and mark it as visited by setting its value to zero. 
This prevents revisiting the same cell and avoids infinite recursion.

Then, we recursively explore all four directions and add their returned areas to the current count.
Finally, we return the maximum island area found in the grid.

**Time Complexity: O(m × n)**
Here, m is the number of rows and n is the number of columns. Each cell is processed at most a constant number of times.
**Space Complexity: O(m × n)**
In the worst case, the recursive call stack can grow to O(m × n) when a large island forms a long DFS path.
"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        r_edge = len(grid)
        c_edge = len(grid[0])

        def dfs(row, col):
            count = 0

            if row >= r_edge or row < 0 or col >= c_edge or col < 0:
                return 0

            if grid[row][col] == 0:
                return 0

            if grid[row][col] == 1:
                count += 1
                grid[row][col] = 0

            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            for r, c in directions:
                r_new = row + r
                c_new = col + c

                count_tmp = dfs(r_new, c_new)
                count = count + count_tmp

            return count

        max_count = 0
        for i in range(0, r_edge):
            for j in range(0, c_edge):
                count = dfs(i, j)
                if count > max_count:
                    max_count = count

        return max_count
