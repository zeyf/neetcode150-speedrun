from collections import deque

class Solution:

    def inbounds(self, x: int, y: int, n: int, m: int):
        return x >= 0 and y >= 0 and x < n and y < m

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        GATE, SAFE = 0, 2147483647


        for x in range(len(rooms)):
            for y in range(len(rooms[x])):
                if rooms[x][y] == GATE:
                    q.append((x, y, 0))

        while len(q) > 0:
            level_size = len(q)

            while level_size > 0:
                cx, cy, source_gate_dist = q.popleft()

                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy

                    if (
                        self.inbounds(nx, ny, len(rooms), len(rooms[0])) and
                        rooms[nx][ny] == SAFE
                    ):
                        rooms[nx][ny] = source_gate_dist + 1
                        q.append((nx, ny, rooms[nx][ny]))

                level_size -= 1

        """
        Do not return anything, modify rooms in-place instead.
        """