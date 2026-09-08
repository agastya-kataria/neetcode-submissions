class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0
        
        for r, ch in enumerate(s):
            if ch in mp:
                l = max(l, mp[ch]+1)
            mp[ch] = r
            res = max(res, r-l+1)
        
        return res
