class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        state = set()
        length = 0

        for end in range(len(s)):
            while s[end] in state:
                state.remove(s[start])
                start += 1
            
            state.add(s[end])
            length = max(length, end - start + 1)
        
        return length


        