# Question No. 242
# Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result_count = [0 for i in range(26)]
        for i in range(len(s)):
            result_count[ord(s[i]) - 97] += 1
        for i in range(len(t)):
            result_count[ord(t[i]) - 97] -= 1

        return all(result_count[i] == 0 for i in range(26))