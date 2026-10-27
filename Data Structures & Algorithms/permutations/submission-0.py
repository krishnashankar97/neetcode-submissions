class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            return [nums]

        def dfs(cur):
            
            #Base case, a permutation is complete only when it holds all the numbers
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):

                if nums[i] in cur:
                    continue
                
                cur.append(nums[i])

                dfs(cur)

                cur.pop()

        dfs([])

        return res


            
