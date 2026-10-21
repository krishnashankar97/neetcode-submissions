class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for s in strs: #n
            x = str(sorted(s)) #nlogn
            if x in hmap: #n
                hmap[x].append(s)
            else:
                hmap[x] = [s]
        
        return list(hmap.values())