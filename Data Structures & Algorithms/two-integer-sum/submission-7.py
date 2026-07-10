class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,n in enumerate(nums):
            if target - n in hmap:
                return sorted([i,hmap[target-n]])
            else:
                hmap[n] = i
        
            