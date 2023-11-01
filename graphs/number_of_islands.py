from collections import deque

class Solution:

    def inbounds(self, x: int, y: int, n: int, m: int):
        return x >= 0 and y >= 0 and x < n and y < m

    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        islands = 0

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    islands += 1
                    grid[x][y] = "0"
                    q.append((x, y))

                    while len(q) > 0:
                        cx, cy = q.popleft()

                        for dx, dy in directions:
                            nx, ny = cx + dx, cy + dy

                            if self.inbounds(nx, ny, len(grid), len(grid[x])) and grid[nx][ny] == "1":
                                grid[nx][ny] = "0"
                                q.append((nx, ny))

        return islands