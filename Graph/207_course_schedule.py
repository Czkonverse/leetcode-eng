"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

"""
I would solve this problem using **DFS to detect cycles in a directed graph**.

First, I'll build an adjacency list from the prerequisites. Each directed edge goes from a prerequisite course to the course that depends on it.

Then, I'll use DFS with three states for each node: unvisited, visiting, and finished.

If DFS encounters a node that is currently visiting, it means we've found a cycle, so it's impossible to finish all courses.

If a node is already finished, we can skip it because we've already checked it.

I'll run DFS on every node to make sure we check the entire graph, including disconnected components.

If we find any cycle, we return false. Otherwise, we return true.

**Time complexity is O(V + E)** because each vertex and edge is processed at most once.

**Space complexity is O(V + E)** for the adjacency list, state array, and recursion stack.
"""


# in dfs function, True means cycle detected, False means not;
# but in canFinish, True means we can finish courses, False means not;
# they are different
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 1 build graph
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        # 0: unvisited
        # 1: visiting
        # 2: finished
        states = [0] * numCourses

        # 2 dfs to detect cycles
        def dfs(node):

            if states[node] == 1:
                return True

            if states[node] == 2:
                return False

            states[node] = 1

            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True

            states[node] = 2
            return False

        # 3 check all nodes
        for node in range(numCourses):
            if dfs(node):
                return False

        return True
