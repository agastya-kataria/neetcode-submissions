class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = 1 + count.get(num,0)
        for num, frequency in count.items():
            freq[frequency].append(num)
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                if len(res)==k:
                    return res
                res.append(n)
        return res