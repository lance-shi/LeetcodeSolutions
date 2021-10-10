# Question No. 201
# Bitwise AND of Numbers Range
# Second try after reading some discussions
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bit_moved = 0
        while left != right:
            left >>= 1
            right >>= 1
            bit_moved += 1

        return left << bit_moved