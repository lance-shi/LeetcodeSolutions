# Question No. 264
# Ugly Number Two
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_list = [1]
        i2 = i3 = i5 = 0
        i = 1
        while i < n:
            new_num = min(ugly_list[i2] * 2, ugly_list[i3] * 3, ugly_list[i5] * 5)
            ugly_list.append(new_num)
            if new_num == ugly_list[i2] * 2:
                i2 += 1
            if new_num == ugly_list[i3] * 3:
                i3 += 1
            if new_num == ugly_list[i5] * 5:
                i5 += 1
            i += 1
        return ugly_list[-1]