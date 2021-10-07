# Question No. 79
# Word Search
class Solution:
    def exist(self, board, word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.b = board
        traveled = [[0 for i in range(self.n)] for i in range(self.m)]
        for k in range(1, len(word)):
            has_char = False
            for i in range(self.m):
                for j in range(self.n):
                    if board[i][j] == word[k]:
                        has_char = True
            if not has_char:
                return False
        start_list = []
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    start_list.append((i, j))
        for i, j in start_list:
            if self.is_valid(i, j, 1, traveled, word):
                return True

        return False

    def find_valid_spots(self, i, j, char, t):
        valid_spots = []
        if i - 1 >= 0 and self.b[i - 1][j] == char and t[i - 1][j] == 0:
            valid_spots.append((i - 1, j))
        if i + 1 < self.m and self.b[i + 1][j] == char and t[i + 1][j] == 0:
            valid_spots.append((i + 1, j))
        if j - 1 >= 0 and self.b[i][j - 1] == char and t[i][j - 1] == 0:
            valid_spots.append((i, j - 1))
        if j + 1 < self.n and self.b[i][j + 1] == char and t[i][j + 1] == 0:
            valid_spots.append((i, j + 1))
        return valid_spots

    def is_valid(self, i, j, n, t, word):
        if n >= len(word):
            return True
        t[i][j] = 1
        char = word[n]
        valid_spots = self.find_valid_spots(i, j, char, t)
        if valid_spots == []:
            t[i][j] = 0
            return False
        for x, y in valid_spots:
            if self.is_valid(x, y, n + 1, t, word):
                return True
        t[i][j] = 0
        return False