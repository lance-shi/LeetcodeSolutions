# Question No. 278
# First Bad Version
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def bSearch(start, end):
            if start >= end:
                if isBadVersion(start):
                    return start
                else:
                    return start + 1
            mid = (start + end) // 2
            if isBadVersion(mid):
                return bSearch(start, mid - 1)
            else:
                return bSearch(mid + 1, end)
        return bSearch(1, n)