# Question No 32
# Longest Valid Parentheses
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        cur_len = 0
        remaining_pos = 0

        for i in range(len(s)):
            if s[i] == "(":
                remaining_pos += 1
            else:
                remaining_pos -= 1

            if remaining_pos < 0:
                remaining_pos = 0
                cur_len = 0
            else:
                cur_len += 1
                if remaining_pos == 0 and cur_len > max_len:
                    max_len = cur_len

        if remaining_pos > 0:
            cur_len = 0
            remaining_pos = 0
            for i in range(1, len(s)):
                if s[-i] == ")":
                    remaining_pos += 1
                else:
                    remaining_pos -= 1
                if remaining_pos < 0:
                    remaining_pos = 0
                    cur_len = 0
                else: 
                    cur_len += 1
                    if remaining_pos == 0 and cur_len > max_len:
                        max_len = cur_len

        return max_len