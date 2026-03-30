class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(0, [], 0, res, target, nums)
        return res

    
    def dfs(self, i, cur, total, res, target, nums):
        if total == target:
            res.append(cur.copy())
            return
        
        if i >= len(nums) or total > target:
            return
        
        cur.append(nums[i])
        self.dfs(i, cur, total + nums[i], res, target, nums)
        cur.pop()
        self.dfs(i + 1, cur, total, res, target, nums)
    


        