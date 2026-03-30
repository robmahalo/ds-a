class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        res = nums[0]

        for i in range(len(nums)):
            curSum = 0
            for j in range(i, i + len(nums)):
                curSum += nums[j % len(nums)]
                res = max(res, curSum)

        return res        