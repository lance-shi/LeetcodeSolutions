# Question No. 4
# Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        x = y = 0
        odd = False if (m + n) % 2 == 0 else True
        target = (m + n) // 2
        lower = 0
        upper = 0
        while x < m and y < n:
            if nums1[x] <= nums2[y]:
                next_one = nums1[x]
                x += 1
            else:
                next_one = nums2[y]
                y += 1
            if x + y == target and not odd:
                lower = next_one
            if x + y == target + 1:
                upper = next_one
        if x + y == target:
            if x == m:
                upper = nums2[y]
            else:
                upper = nums1[x]
        if x + y < target:
            gap = target - x - y
            if x == m:
                upper = nums2[y + gap]
                if not odd:
                    lower = nums2[y + gap - 1]
            else:
                upper = nums1[x + gap]
                if not odd:
                    lower = nums1[x + gap - 1]
        return float(upper) if odd else (upper + lower) / 2