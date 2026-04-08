class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_map = {}
        
        for char in s:
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1
        
        for char in t:
            if char in freq_map:
                freq_map[char] -= 1
            else:
                return False
        
        for val in freq_map.values():
            if val != 0:
                return False
        
        return True

        