class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1, hmap2 = {}, {}
        for c in s:
            if c in hmap1:
                hmap1[c] += 1
            else:
                hmap1[c] = 1
        for a in t:
            if a in hmap2:
                hmap2[a] += 1
            else:
                hmap2[a] = 1
        return hmap1 == hmap2
        