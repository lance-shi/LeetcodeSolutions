# Question No. 980
# Unique Paths Three
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        white = 0
        self.m = len(grid)
        self.n = len(grid[0])
        startx = starty = 0
        self.count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    white += 1
                elif grid[i][j] == 1:
                    startx = i
                    starty = j
        self.dfs(grid, white, startx, starty)
        return self.count

    def dfs(self, grid, white, cx, cy):
        directions = [0, 1, 0, -1, 0]
        if grid[cx][cy] == 0:
            grid[cx][cy] = -1
        for i in range(4):
            x = cx + directions[i]
            y = cy + directions[i + 1]
            if x < 0 or y < 0 or x >= self.m or y >= self.n:
                continue
            if grid[x][y] == 2 and white == 0:
                self.count += 1
                grid[cx][cy] = 0
                return
            if grid[x][y] == 0:
                self.dfs(grid, white - 1, x, y)
            else:
                continue
        if grid[cx][cy] == -1:
            grid[cx][cy] = 0