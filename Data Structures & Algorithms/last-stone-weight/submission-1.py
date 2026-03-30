class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        n = len(stones)

        while len(stones) > 1:
            curStone = stones.pop() - stones.pop()
            n -= 2

            if curStone > 0:
                left = 0
                right = n

                while left < right:
                    mid = (left + right) // 2

                    if stones[mid] < curStone:
                        left = mid + 1
                    else:
                        right = mid
                
                pos = left
                n += 1
                stones.append(0)

                for i in range(n - 1, pos, -1):
                    stones[i] = stones[i - 1]
                stones[pos] = curStone
            
        return stones[0] if n > 0 else 0
        