class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        last = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= last
            last *= nums[i]

        last = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= last
            last *= nums[i]

        return res