# Question No. 130
# Surrounded Regions
class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        directions = [0, 1, 0, -1, 0]
        starting = []
        for i in range(n):
            if board[0][i] == "O":
                board[0][i] = "Z"
                starting.append((0, i))
            if board[m - 1][i] == "O":
                board[m - 1][i] = "Z"
                starting.append((m - 1, i))
        for i in range(m):
            if board[i][0] == "O":
                board[i][0] = "Z"
                starting.append((i, 0))
            if board[i][n - 1] == "O":
                board[i][n - 1] = "Z"
                starting.append((i, n - 1))
        while starting:
            temp = []
            for (cx, cy) in starting:
                for i in range(4):
                    x = cx + directions[i]
                    y = cy + directions[i + 1]
                    if x < 0 or y < 0 or x >= m or y >= n:
                        continue
                    if board[x][y] == "O":
                        board[x][y] = "Z"
                        temp.append((x, y))
            starting = temp
        for i in range(m):
            for j in range(n):
                if board[i][j] == "Z":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"