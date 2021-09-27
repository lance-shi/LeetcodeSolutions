class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        answer = [3,1,2]
        while len(answer) < n:
            answer = [(2*i-1) for i in answer] + [2*i for i in answer]
        return [i for i in answer if i <= n]