class Solution:
    def tictactoe(self, moves):
        self.tiles = [[0 for i in range(3)] for i in range(3)]
        previous = -1
        for i in range(len(moves)):
            [row, col] = moves[i]
            previous = -previous
            self.tiles[row][col] = previous

        result = self.get_winner()
        if result == 1:
            return "A"
        elif result == -1:
            return "B"
        elif len(moves) == 9:
            return "Draw"
        else:
            return "Pending"

    def get_winner(self):
        if self.tiles[0][0] == self.tiles[1][1] and self.tiles[1][1] == self.tiles[2][2]:
            return self.tiles[0][0]
        if self.tiles[2][0] == self.tiles[1][1] and self.tiles[1][1] == self.tiles[0][2]:
            return self.tiles[2][0]
        for i in range(3):
            if self.tiles[i][0] == self.tiles[i][1] and self.tiles[i][1] == self.tiles[i][2]:
                return self.tiles[i][0]
        for i in range(3):
            if self.tiles[0][i] == self.tiles[1][i] and self.tiles[1][i] == self.tiles[2][i]:
                return self.tiles[0][i]
        return 0