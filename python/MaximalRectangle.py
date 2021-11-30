# Question No. 85
# Maximal Rectangle
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        max_area = 0
        def max_at_point(x, y):
            nonlocal max_area
            i = 0
            while i + x < m and matrix[x + i][y] == "1":
                i += 1
            cur_len = i
            cur_wid = 1
            max_area = max(max_area, cur_len)
            j = 0
            while j + y < n and matrix[x][y + j] == "1":
                j += 1
            max_wid = j
            if max_wid * cur_len <= max_area:
                return
            for j in range(1, max_wid):
                i = 0
                while i < cur_len and matrix[x + i][y + j] == "1":
                    i += 1
                cur_len = i
                max_area = max(max_area, cur_len * (j + 1))
                if max_area >= cur_len * max_wid:
                    break
        for i_p in range(m):
            for j_p in range(n):
                if matrix[i_p][j_p] == "1":
                    max_at_point(i_p, j_p)
        return max_area