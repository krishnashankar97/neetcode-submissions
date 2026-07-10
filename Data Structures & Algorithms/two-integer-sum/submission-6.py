class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        ans = []
        for i,j in enumerate(nums):
            
            if target - j in hmap:
                if i < hmap[target - j]:
                    return [i,hmap[target - j]]
                return [hmap[target - j],i]
            else:
                hmap[j] = i
            