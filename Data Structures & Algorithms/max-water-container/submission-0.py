class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        vol = float('-inf')
        while l < r:
            v = min(heights[l],heights[r])*(r-l)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
            vol = max(vol, v)
        return vol
