class Solution:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.arbitrary_edge_connected_island_flip_value = "Z"

    def inbounds(self, x: int, y: int, n: int, m: int):
        return x >= 0 and y >= 0 and x < n and y < m

    ## perform a dfs and flip edge connected islands completely to an arbitrary non {"O", "X"} value
    def dfs_flip(self, board, x, y):
        board[x][y] = self.arbitrary_edge_connected_island_flip_value

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy

            if self.inbounds(nx, ny, len(board), len(board[0])) and board[nx][ny] == "O":
                self.dfs_flip(board, nx, ny)

    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])

        for row in range(n):
            if board[row][0] == "O":
                self.dfs_flip(board, row, 0)
            
            if board[row][m - 1] == "O":
                self.dfs_flip(board, row, m - 1)
        
        for col in range(m):
            if board[0][col] == "O":
                self.dfs_flip(board, 0, col)
            
            if board[n - 1][col] == "O":
                self.dfs_flip(board, n - 1, col)
        
        for x in range(n):
            for y in range(m):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == self.arbitrary_edge_connected_island_flip_value:
                    board[x][y] = "O"

        """
        Do not return anything, modify board in-place instead.
        """
        