import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        m = n * 2
        sqt = math.floor(math.sqrt(m))
        if m < (sqt - 1) * sqt:
            return sqt - 2
        if m < (sqt + 1) * sqt:
            return sqt - 1
        if m < (sqt + 1) * (sqt + 2):
            return sqt 
        return sqt + 1