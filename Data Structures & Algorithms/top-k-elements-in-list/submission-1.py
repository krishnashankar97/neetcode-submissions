class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            if n in hmap: hmap[n]+=1
            else: hmap[n] = 1
        hmap_sorted = dict(sorted(hmap.items(), key=lambda item: item[1],reverse=True))
        return list(hmap_sorted.keys())[0:k]