# Question No. 496
# Next Greater Element
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, next_map = [], dict()
        for num in nums2[::-1]:
            while stack and num > stack[-1]:
                stack.pop()
            next_map[num] = stack[-1] if stack else -1
            stack.append(num)
        for i, num in enumerate(nums1):
            nums1[i] = next_map[num]
        return nums1
