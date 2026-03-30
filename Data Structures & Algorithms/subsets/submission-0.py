class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        i = 0

        self.dfs(i, res, subset, nums)
        return res

    def dfs(self, i, res, subset, nums):
        if i >= len(nums):
            res.append(subset.copy())
            return
        
        subset.append(nums[i])
        self.dfs(i + 1, res, subset, nums)
        subset.pop()
        self.dfs(i + 1, res, subset, nums)
        