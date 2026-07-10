class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = dict(Counter(nums))
        ans = []
        sorted_dict = dict(sorted(hmap.items(), key=lambda item: item[1], reverse=True))
        l = list(sorted_dict.keys())
        return l[:k]