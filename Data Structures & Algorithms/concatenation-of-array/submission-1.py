class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(nums):
            res.append(n)
        for i, n in enumerate(nums):
            res.append(n)
        return res