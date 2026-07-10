class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums)
        desc_hmap = dict(sorted(hmap.items(), key=lambda item: item[1], reverse=True))
        li = list(desc_hmap.keys())
        return li[:k]