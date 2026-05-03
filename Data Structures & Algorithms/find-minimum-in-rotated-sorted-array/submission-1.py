class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        for i in range(len(nums)):
            curr_num = nums[i]
            res = min(curr_num, res)
        
        return res

        