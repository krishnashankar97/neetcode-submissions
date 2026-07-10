class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        ans = []
        for i,c in enumerate(nums):
            if target - c in hmap:
                ans = [hmap[target - c], i]
            else:
                hmap[c] = i
        return ans