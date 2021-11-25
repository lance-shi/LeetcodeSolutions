# Question No. 986
# Interval List Intersections
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        a = b = 0
        start = -1
        while a < len(firstList) and b < len(secondList):
            if firstList[a][1] < secondList[b][0]:
                a += 1
                continue
            if secondList[b][1] < firstList[a][0]:
                b += 1
                continue
            if firstList[a][0] < secondList[b][0]:
                start = secondList[b][0]
            else:
                start = firstList[a][0]
            if firstList[a][1] < secondList[b][1]:
                end = firstList[a][1]
                a += 1
            else:
                end = secondList[b][1]
                b += 1
            result.append([start, end])
        return result