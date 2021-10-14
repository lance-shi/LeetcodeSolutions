# Question No. 279
# Perfect Squares
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, 101)]
        min_list = [i for i in range(n + 1)]
        cur_max_square = 1
        for i in range(1, n + 1):
            if i == square_nums[cur_max_square]:
                cur_max_square += 1
                min_list[i] = 1
                continue
            for j in range(cur_max_square):
                min_list[i] = min(min_list[i], 1 + min_list[i - square_nums[j]])
        return min_list[n]