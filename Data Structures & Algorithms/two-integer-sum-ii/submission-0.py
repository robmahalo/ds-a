class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1        

        while left < right:
            match = numbers[left] + numbers[right]

            if match == target:
                return [left + 1, right + 1]
            
            if target > match:
                left += 1
            elif target < match:
                right -= 1
        
        return []
            
        