# Question No. 62
# Unique Paths
import math
class Solution:
    def comb(self, x, y):
        return math.factorial(x) // (math.factorial(y) * math.factorial(x - y))
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n:
            m, n = n, m
        if n == 1:
            return 1
        return comb(n + m - 2, m - 1)