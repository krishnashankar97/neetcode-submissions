class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for c in strs:
            x = ''.join(sorted(c))
            if x in hmap:
                hmap[x].append(c)
            else:
                hmap[x] = [c]
        return hmap.values()