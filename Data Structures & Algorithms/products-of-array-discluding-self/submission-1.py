class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*(len(nums))
        prev = 1
        n = 1
        for i in range(len(nums)):
            res[i] = prev
            prev *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i]*= n
            n *= nums[i]
        return res