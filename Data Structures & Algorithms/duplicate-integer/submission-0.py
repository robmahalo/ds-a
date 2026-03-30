class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []

        for num in range(len(nums)):
            if nums[num] in seen:
                return True
            seen.append(nums[num])
        
        return False
        
        
        
        