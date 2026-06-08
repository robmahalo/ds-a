class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = 0

        while left <= right:
            totalTime = 0
            mid = left + (right - left) // 2
            for p in piles:
                totalTime += (p + mid - 1) // mid
            
            if totalTime <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res
        