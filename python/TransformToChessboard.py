# Question No. 782
# Transform to Chessboard
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        N = len(board)
        if any(board[0][0]^board[i][0]^board[0][j]^board[i][j] for i in range(N) for j in range(N)):
            return -1
        if not N/2 <= sum(board[0]) <= (N+1)/2:
            return -1
        if not N/2 <= sum(board[i][0] for i in range(N)) <= (N+1)/2:
            return -1

        col = sum(board[0][i] == i % 2 for i in range(N))
        row = sum(board[i][0] == i % 2 for i in range(N))

        if N % 2:
            if col % 2: 
                col = N - col
            if row % 2: 
                row = N - row
        else:
            col = min(N - col, col)
            row = min(N - row, row)

        return (col + row) // 2