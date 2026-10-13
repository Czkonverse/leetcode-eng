"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        grid_row = len(grid)
        grid_col = len(grid[0])

        def dfs(row, col):
            if row >= grid_row or row < 0 or col >= grid_col or col < 0:
                return

            if grid[row][col] == "0":
                return

            if grid[row][col] == "1":
                grid[row][col] == "0"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        islands = 0
        for row in range(grid_row):
            for col in range(grid_col):
                if grid[row][col] == "1":
                    islands += 1
                dfs(row, col)

        return islands
