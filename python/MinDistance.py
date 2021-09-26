# This is Leetcode question Number 583: Delete Operaion for Two Strings
# This is actually a Longest Common Sequence question
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        lcs = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    lcs[i+1][j+1] = lcs[i][j] + 1
                else:
                    lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j])
        return m + n - 2 * lcs[i+1][j+1]