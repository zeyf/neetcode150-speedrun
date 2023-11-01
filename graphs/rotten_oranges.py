from collections import deque

class Solution:

    def inbounds(self, x: int, y: int, n: int, m: int):
        return x >= 0 and y >= 0 and x < n and y < m

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_q = deque()
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        EMPTY, FRESH, ROTTEN = 0, 1, 2
        total_fresh_count = 0

        ## add all rotten orange locations to a queue for level wise processing
        ## count the fresh oranges to know at the end if we got to rot all of them
        ## as we visit or "rot" a fresh orange, we will decrement that count
        for x in range(n):
            for y in range(m):
                if grid[x][y] == ROTTEN:
                    rotten_q.append((x, y))
                else:
                    total_fresh_count += grid[x][y]

        ## the "minutes" are really the # of levels needed to rot all fresh oranges reachable
        minutes = 0
        while len(rotten_q) > 0:
            level_size = len(rotten_q)
            
            ## we need to keep track of this to know if we add a minute or not
            ## if false after attempting to spread, we know we cannot process anything further
            spread = False

            for _ in range(level_size):
                cx, cy = rotten_q.popleft()

                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy

                    if self.inbounds(nx, ny, n, m) and grid[nx][ny] == FRESH:
                        total_fresh_count -= 1
                        grid[nx][ny] = ROTTEN
                        rotten_q.append((nx, ny))
                        spread = True
            
            if not spread:
                break
            
            minutes += 1
        
        ## only if we rotted all fresh oranges
        ## meaning that all fresh oranges were in a connected component to a rotten orange
        return minutes if total_fresh_count == 0 else -1