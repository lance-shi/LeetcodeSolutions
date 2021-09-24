class Solution:
    def tribonacci(self, n: int) -> int:
        answer_list = [0 for i in range(38)]
        answer_list[1] = 1
        answer_list[2] = 1
        for i in range(3, n+1):
            answer_list[i] = answer_list[i-1] + answer_list[i-2] + answer_list[i-3]
        return answer_list[n]