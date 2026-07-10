class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap_s = {}
        hmap_t = {}
        for i,n in enumerate(s):
            if n in hmap_s:
                hmap_s[n] += 1
            else:
                hmap_s[n] = 1
            
        for i,n in enumerate(t):
            if n in hmap_t:
                hmap_t[n] += 1
            else:
                hmap_t[n] = 1

        return hmap_s == hmap_t