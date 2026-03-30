class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        state = []
        length = 0

        for end in range(len(s)):
            while s[end] in state:
                state.remove(s[start])
                start += 1
            
            state.append(s[end])
            length = max(length, len(state))
        
        return length


        