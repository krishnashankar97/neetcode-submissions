class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #minHeap declare and populate
        minHeap = []
        for x,y in points:
            #First calculate distance
            dist = (x**2) + (y**2)
            minHeap.append([dist,x,y])
        
        #convert it to minHeap datastructure
        heapq.heapify(minHeap)
        res = []
        #Second heappop K nearest points
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        return res 