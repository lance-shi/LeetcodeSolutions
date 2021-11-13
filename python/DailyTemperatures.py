# Question No. 739
# Daily Temperatures
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        result = [0 for i in range(n)]
        heap = []
        for i in range(n):
            while heap:
                if temperatures[i] > heap[-1][0]:
                    result[heap[-1][1]] = i - heap[-1][1]
                    heap.pop()
                else:
                    break
            heap.append((temperatures[i], i))
        return result