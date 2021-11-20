# Question No. 461
# Hamming Distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        result = 0
        while diff != 0:
            result += diff % 2
            diff >>= 1
        return result