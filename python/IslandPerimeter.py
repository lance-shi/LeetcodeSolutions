# Question No. 463
# Island Perimeter
class Solution:
    def islandPerimeter(self, grid) -> int:
        perimeter = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j]:
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1]:
                        perimeter -= 2

        return perimeter