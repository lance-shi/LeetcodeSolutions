# Question No. 174
# Dungeon Game
class Solution:
    def calculateMinimumHP(self, dungeon) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dungeon[m - 1][n - 1] = max(1, -dungeon[m - 1][n - 1] + 1)
        for i in range(m - 2, -1, -1):
            dungeon[i][n - 1] = max(1, -dungeon[i][n - 1] + dungeon[i + 1][n - 1])
        for j in range(n - 2, -1, -1):
            dungeon[m - 1][j] = max(1, -dungeon[m - 1][j] + dungeon[m - 1][j + 1])
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dungeon[i][j] = max(1, -dungeon[i][j] + min(dungeon[i][j + 1], dungeon[i + 1][j]))

        return dungeon[0][0]