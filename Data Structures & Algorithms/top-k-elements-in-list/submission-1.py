class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        state = {}
        heap = []

        for i in nums:
            state[i] = state.get(i, 0) + 1
        
        for num in state.keys():
            heapq.heappush(heap, (state[num], num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
