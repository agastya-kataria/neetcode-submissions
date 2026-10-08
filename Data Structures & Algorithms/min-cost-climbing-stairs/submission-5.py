class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev2 = cost[0]
        prev = cost[1]

        for i in range(2,n):
            tmp = cost[i] + min(prev, prev2)
            prev2 = prev
            prev = tmp
        return min(prev, prev2)