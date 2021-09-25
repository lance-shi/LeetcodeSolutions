class Solution:
    def shortestPath(self, grid, k: int) -> int:
        directions = [0, 1, 0, -1, 0]
        n = len(grid)
        m = len(grid[0])
        seen = [[k+1 for i in range(m)] for i in range(n)]
        cur_queue = [(0, 0, 0)]
        steps = 0

        while len(cur_queue) > 0:
            tmp_queue = cur_queue
            cur_queue = []
            for i in range(len(tmp_queue)):
                (cx, cy, rank) = tmp_queue[i]
                if cx == m - 1 and cy == n - 1:
                    return steps

                for i in range(4):
                    x = cx + directions[i]
                    y = cy + directions[i + 1]
                    if x < 0 or y < 0 or x >= m or y >= n:
                        continue
                    added_rank = rank + grid[y][x]
                    if added_rank > k or added_rank >= seen[y][x]:
                        continue
                    seen[y][x] = added_rank
                    cur_queue.append((x, y, added_rank))

            steps += 1

        return -1