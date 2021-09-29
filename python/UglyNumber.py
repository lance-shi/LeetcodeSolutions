# Question No. 263
# Ugly Number
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while not n % 5:
            n = n // 5
        while not n % 3:
            n = n // 3
        while not n % 2:
            n = n // 2
        return n == 1