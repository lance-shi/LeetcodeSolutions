# Question No. 451
# Sort Characters by Frequency
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        result = ""
        for ch, i in c.most_common():
            result += ch * i
        return result