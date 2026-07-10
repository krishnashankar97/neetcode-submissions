class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,n in enumerate(nums): 
            if target - n in hmap:
                if i < hmap[target - n]:
                    return [i,hmap[target - n]]
                else:
                    return [hmap[target - n],i]
            else:
                hmap[n] = i
            
