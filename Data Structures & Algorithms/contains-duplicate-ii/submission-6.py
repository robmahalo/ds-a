class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        start = 0

        for end in range(len(nums)):
            if end - start > k:
                seen.remove(nums[start])
                start += 1
                
            if nums[end] in seen:
                return True

            seen.add(nums[end])

            

        return False
        