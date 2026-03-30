class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            curStone = stones.pop() - stones.pop()

            if curStone:
                stones.append(curStone)
        
        return stones[0] if stones else 0
        