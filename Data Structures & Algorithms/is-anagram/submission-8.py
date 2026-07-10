class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmaps = {}
        hmapt = {}
        for c in s:
            if c in hmaps: hmaps[c] += 1
            else: hmaps[c] = 1
        
        for c in t:
            if c in hmapt: hmapt[c] += 1
            else: hmapt[c] = 1
        
        return hmaps == hmapt