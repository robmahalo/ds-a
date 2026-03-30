class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()
        left = 0
        right = len(nums) - 1

        while left < right:
            match = A[left][0] + A[right][0]
            if match == target:
                return [min(A[left][1], A[right][1]), max(A[left][1], A[right][1])]
            elif match < target:
                left += 1
            else:
                right -= 1
        
        return []
        