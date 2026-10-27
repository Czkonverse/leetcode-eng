"""
My approach is to use Depth-First Search (DFS).

We start from room 0, which is initially unlocked.

For each room, we collect its keys and recursively explore the rooms that those keys can unlock.

We use a set called `visited` to keep track of the rooms we've already discovered. This prevents us from visiting the same room multiple times and avoids infinite recursion when there are cycles.

Finally, we check whether the number of visited rooms equals the total number of rooms.

**Time Complexity: O(V + E)**

Here, V is the number of rooms, and E is the total number of keys.

Each room is visited at most once, and each key is examined at most once.

**Space Complexity: O(V)**

The visited set stores at most V room indices, and the recursive call stack can grow to O(V) in the worst case.
"""


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = {0}

        def dfs(room):
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    dfs(key)

        dfs(0)

        return len(visited) == len(rooms)


from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        queue = deque([0])
        visited = {0}

        while queue:
            room = queue.popleft()

            for k in rooms[room]:
                if k not in visited:
                    visited.add(k)
                    queue.append(k)

        return len(visited) == len(rooms)
