class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,v in enumerate(nums):
            if target - v in hmap:
                if i < hmap[target-v]:
                    return [i,hmap[target-v]]
                else:
                    return [hmap[target-v],i]
            else:
                hmap[v] = i

        