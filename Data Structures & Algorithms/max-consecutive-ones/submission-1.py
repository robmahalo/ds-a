class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for i in nums:
            if i == 0:
                res = max(res, count)
                count = 0
            else:
                count += 1

        return max(count, res)
        