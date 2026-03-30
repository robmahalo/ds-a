class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, total = 0,0
        length = float('inf')

        for end in range(len(nums)):
            total += nums[end]

            while total >= target:
                length = min(length, end - start + 1)
                total -= nums[start]
                start += 1
            
        return length if length != float('inf') else 0