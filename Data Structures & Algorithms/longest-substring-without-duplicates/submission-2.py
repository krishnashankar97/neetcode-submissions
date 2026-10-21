class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        hm = {}
        for r in range(len(s)):
            if s[r] in hm:
                l = max(l,hm[s[r]]+1)
            hm[s[r]] = r
            res = max(res,r-l+1)
        return res