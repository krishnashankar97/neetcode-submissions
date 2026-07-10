class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            x = ''.join(sorted(s))
            if x in hmap:
                hmap[x].append(s)
            else:
                hmap[x] = [s]
        return hmap.values()