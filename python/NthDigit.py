# Question No. 400
# Nth Digit
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 0
        for i in range(11):
            cur_total = (i + 1) * (10 ** i) * 9
            if n > cur_total:
                n -= cur_total
            else:
                digit = i + 1
                break
        index, remainder = divmod(n - 1, digit)
        cur_num = 10 ** (digit - 1) + index
        digit_from_down = digit - 1 - remainder
        for i in range(digit_from_down):
            cur_num = cur_num // 10
        return cur_num % 10