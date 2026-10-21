class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = dict(Counter(nums))
        heap = []
        for n in hmap.keys():
            heapq.heappush(heap, (hmap[n], n))

            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
            

