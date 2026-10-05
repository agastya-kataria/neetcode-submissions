class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))

    def rob_helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            tmp = max(rob2, rob1+n)
            rob1 = rob2
            rob2 = tmp
        return rob2