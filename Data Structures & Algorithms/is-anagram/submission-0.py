class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        state = {}
        
        for i in range(len(s)):
            state[s[i]] = state.get(s[i], 0) + 1
        
        for j in range(len(t)):
            state[t[j]] = state.get(t[j], 0) - 1
        
        for val in state.values():
            if val != 0:
                return False
        
        return True

        