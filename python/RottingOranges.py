# Question No.994
# Rotting Oranges
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [0, 1, 0, -1, 0]
        fresh = 0
        day = 0
        rot = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rot.append((i, j))
        if fresh == 0:
            return day

        while rot:
            if fresh == 0:
                return day
            day += 1
            rotting = []
            for cx, cy in rot:
                for i in range(4):
                    x = cx + directions[i]
                    y = cy + directions[i + 1]
                    if x < 0 or y < 0 or x >= m or y >= n:
                        continue
                    if grid[x][y] == 1:
                        rotting.append((x, y))
                        fresh -= 1
                        grid[x][y] = 2
            rot = rotting

        return -1


