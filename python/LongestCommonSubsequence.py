# Question No 1143
# Longest Common Subsequence
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        lcs = [[0 for i in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    lcs[i+1][j+1] = lcs[i][j] + 1
                else:
                    lcs[i+1][j+1] = max(lcs[i][j+1], lcs[i+1][j])
        return lcs[i+1][j+1]