class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmaps = {}
        for c in s:
            if c in hmaps: hmaps[c] += 1
            else: hmaps[c] = 1
        
        for c in t:
            if c in hmaps: hmaps[c] -= 1
            else: return False
        v = list(hmaps.values())

        if v.count(0) == len(v):
            return True
        else:
            return False
        