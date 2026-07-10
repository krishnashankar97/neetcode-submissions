class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        l = 0
        ct = {}
        ans = 0
        for r in range(len(s)):
            ct[s[r]] = 1+ct.get(s[r],0)
            maxF = max(maxF,ct[s[r]])

            while (r-l+1) - maxF > k:
                ct[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        
        return ans