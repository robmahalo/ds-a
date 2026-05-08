class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        state = {}

        for end in range(len(s)):
            if s[end] in state:
                start = max(state[s[end]] + 1, start)
            state[s[end]] = end
            max_length = max(max_length, end - start + 1)
        
        return max_length

        