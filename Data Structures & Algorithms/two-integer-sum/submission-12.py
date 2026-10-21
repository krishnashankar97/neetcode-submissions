class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,v in enumerate(nums):
            if target - v in hmap:
                return [hmap[target-v],i]
            else:
                hmap[v] = i

        