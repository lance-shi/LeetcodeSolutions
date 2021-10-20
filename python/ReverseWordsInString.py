# Question No. 151
# Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split()
        return " ".join(word_list[::-1])