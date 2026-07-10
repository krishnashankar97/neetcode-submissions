class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i,n in enumerate(nums):
            if n in hmap: return True
            else:
                hmap[n] = 1
        return False