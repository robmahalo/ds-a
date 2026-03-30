class NumArray:
    def __init__(self, nums: List[int]):
        self.val = []
        for i in range(len(nums)):
            self.val.append(nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += self.val[i]
        return sum

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)