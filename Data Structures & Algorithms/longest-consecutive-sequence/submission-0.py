class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        ct = 0
        max_ct = 0
        for n in nums:
            if n-1 not in numSet:
                ct = 0
                while n+ct in numSet:
                    ct += 1
            max_ct = max(ct,max_ct)
        return max_ct