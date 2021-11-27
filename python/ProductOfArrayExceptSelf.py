# Question No. 238
# Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for i in range(n)]
        has_zero = False
        prod_all = 1
        zero_index = -1
        for i in range(n):
            if nums[i] == 0:
                if has_zero:
                    return ans
                else:
                    has_zero = True
                    zero_index = i
                    continue
            prod_all *= nums[i]
        if has_zero:
            ans[zero_index] = prod_all
            return ans
        for i in range(n):
            ans[i] = prod_all // nums[i]
        return ans