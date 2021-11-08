# Question No. 96 
# Unique Binary Search Trees
class Solution:
    def numTrees(self, n: int) -> int:
        F = [1, 1, 2, 5]
        if n >= 4:
            for i in range(4, n + 1):
                cur = 0
                for j in range(i):
                    k = i - 1 - j
                    cur += F[j] * F[k]
        return F[n]