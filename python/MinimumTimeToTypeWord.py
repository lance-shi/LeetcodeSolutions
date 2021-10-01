# Question No. 1974
# Minimum Time to Type Word Using Special Typewriter
class Solution:
    def minTimeToType(self, word: str) -> int:
        init_gap = ord(word[0]) - ord("a")
        over_all = min(init_gap, 26 - init_gap)
        for i in range(1, len(word)):
        	gap = abs(ord(word[i]) - ord(word[i-1]))
        	over_all += min(gap, 26 - gap)
        return over_all + len(word) 
        # key to better efficiency is to add len(word) in the end instead of adding 1 each time