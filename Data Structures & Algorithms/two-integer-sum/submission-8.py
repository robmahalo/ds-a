class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, n in enumerate(nums):
            match = target - n

            if match in map:
                return[map[match], i]
            map[n] = i
        