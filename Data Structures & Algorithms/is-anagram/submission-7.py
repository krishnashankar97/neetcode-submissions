class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1 = Counter(s)
        hmap2 = Counter(t)

        return hmap1 == hmap2
