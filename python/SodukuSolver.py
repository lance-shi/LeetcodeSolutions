# Question No. 37
# Sudoku Solver
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        find = self.find_empty(board)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(board, str(i), (row, col)):
                board[row][col] = str(i)

                if self.solveSudoku(board):
                    return True

                board[row][col] = '.'

        return False
    
    def valid(self, bo, num, pos):
        # Check row
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if bo[i][j] == num and (i,j) != pos:
                    return False

        return True

    def find_empty(self, bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == '.':
                    return (i, j)  # row, col

        return None