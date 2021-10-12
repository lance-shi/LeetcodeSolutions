# Question No. 374
# Guess Number Higher or Lower

class Solution:
    def guessNumber(self, n: int) -> int:
        min_num = 1
        max_num = n
        cur_pick = (min_num + max_num) // 2
        while True:
            r = guess(cur_pick)
            if r == 0:
                return cur_pick
            elif r == -1:
                max_num = cur_pick - 1
            else:
                min_num = cur_pick + 1
            cur_pick = (min_num + max_num) // 2
            r = guess(cur_pick)
        return cur_pick
        