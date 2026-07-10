class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,n in enumerate(nums):
            if target - n in hmap:
                if hmap[target-n] < i:
                    return [hmap[target-n],i]
                else:
                    return [i,hmap[target-n]]
            else:
                hmap[n] = i