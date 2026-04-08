class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        res = []
        sorted_list = []

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num, cnt in freq_map.items():
            sorted_list.append([cnt, num])
        
        sorted_list.sort()

        while len(res) < k:
            res.append(sorted_list.pop()[1])
        
        return res
        