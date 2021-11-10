class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        n, m = len(words), len(puzzles)
        result = [0 for i in range(m)]
        for i in range(m):
            arr = [0] * 26
            for j in range(len(puzzles[i])):
                arr[ord(puzzles[i][j]) - 91] = 1
            for j in range(n):
                has_first = False
                contain = True
                for k in range(len(words[j])):
                    if arr[ord(words[j][k]) - 91] != 1:
                        contain = False
                        break
                    if words[j][k] == puzzles[i][0]:
                        has_first = True

                if has_first and contain:
                    result[i] += 1
        return result
