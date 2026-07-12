class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i,x in enumerate(nums):
            diff = target - x
            if diff in nmap:
                return [nmap[diff], i]
            nmap[x] = i