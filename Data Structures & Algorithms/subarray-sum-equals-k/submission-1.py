class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = {0:1}
        cs = 0
        ct = 0
        for num in nums:
            cs += num
            ct += prefix_sum.get(cs - k,0)
            prefix_sum[cs] = prefix_sum.get(cs,0) + 1

        return ct