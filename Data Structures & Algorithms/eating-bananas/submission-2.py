class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            hours = 0

            for bananas in piles:
                hours += math.ceil(float(bananas) / mid)
            
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
        
        