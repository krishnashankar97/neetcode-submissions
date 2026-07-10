class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums)

        sorted_hmap = dict(sorted(hmap.items(), key=lambda item: item[1]))

        return list(sorted_hmap.keys())[-k:]