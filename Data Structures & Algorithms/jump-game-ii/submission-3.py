class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")]* len(nums)
        dp[len(nums)-1] = 0
        for i in range(len(nums)-2,-1,-1):
            
            if i+nums[i]==len(nums):
                dp[i] = 1
                continue
            for j in range(i+1,i+nums[i]+1):
                if j <len(nums):
                    dp[i] = min(dp[i], 1+dp[j])
        return dp[0]
            