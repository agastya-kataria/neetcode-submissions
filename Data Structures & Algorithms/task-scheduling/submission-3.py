class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0]*26
        for i in tasks:
            count[ord(i)-ord("A")]+=1
        count.sort()
        maxf = count[25]
        idle = n*(maxf-1)
        for i in range(24, -1, -1):
            idle -= min(count[i], maxf - 1)
        return max(0,idle) + len(tasks)