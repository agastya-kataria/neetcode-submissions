class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)//2
        if sum(nums)%2: return False
        dp = set()
        dp.add(0)

        for n in nums:
            nextDP = set()
            for t in dp:
                nextDP.add(t+n)
                nextDP.add(t)
            dp = nextDP
        return target in dp