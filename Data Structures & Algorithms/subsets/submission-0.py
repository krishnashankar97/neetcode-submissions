class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        #[1,2,3]
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1)

            #Decision to not include nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res