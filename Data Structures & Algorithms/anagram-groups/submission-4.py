class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for w in strs:
            key = "".join(sorted(w))
            if key in hmap:
                hmap[key].append(w)
            else:
                hmap[key] = [w]
        return list(hmap.values())