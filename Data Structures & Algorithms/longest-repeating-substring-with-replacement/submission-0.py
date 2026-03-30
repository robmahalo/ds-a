class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        state = {}
        start = 0
        max_length = 0

        for end in range(len(s)):
            state[s[end]] = state.get(s[end], 0) + 1
            
            while (end - start + 1) - max(state.values()) > k:
                state[s[start]] -= 1
                start += 1
            
            max_length = max(max_length, end - start + 1)
        
        return max_length