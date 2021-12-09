# Question No. 1306
# Jump Game Three
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        l = [start]
        while l:
            tmp = []
            for p in l:
                if arr[p] == 0:
                    return True
                if p + arr[p] < n and arr[p + arr[p]] != -1:
                    tmp.append(arr[p] + p)
                if p - arr[p] >= 0 and arr[p - arr[p]] != -1:
                    tmp.append(p - arr[p])
                arr[p] = -1
            l = tmp
        return False