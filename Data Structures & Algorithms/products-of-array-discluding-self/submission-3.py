class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lres = [1] * (len(nums))
        for i in range(1,len(nums)):
            lres[i] = nums[i-1] * lres[i-1]
        rres = [1]*(len(nums))
        for i in range(len(nums)-2, -1, -1):
            rres[i] = rres[i+1]*nums[i+1]
        ans = []
        for i in range(len(lres)):
            ans.append(lres[i]*rres[i])
        return ans
        

        