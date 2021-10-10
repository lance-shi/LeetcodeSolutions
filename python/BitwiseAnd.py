# Question No. 201
# Bitwise AND of Numbers Range
# My initial try - It is pretty slow but still in acceptable range
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        self.power_list = [1 << i for i in range(32)]
        digit_list = []
        while self.get_digit(left, right) != -1:
            digit = self.get_digit(left, right)
            digit_list.append(digit)
            left -= self.power_list[digit]
            right -= self.power_list[digit]
        return sum(self.power_list[i] for i in digit_list)

    def get_digit(self, left, right):
        if left == 0:
            return -1
        i = 0
        while i < 32:
            if left < self.power_list[i]:
                break
            i += 1
        if i == 31:
            return 30
        elif right >= self.power_list[i]:
            return -1
        else:
            return i - 1