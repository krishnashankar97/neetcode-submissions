class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) 
        while r < len(s2) + 1:
            if Counter(s1) == Counter(s2[l:r]):
                return True
            l += 1
            r += 1
        return False