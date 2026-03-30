class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        seen = {}

        for val in range(len(s)):
            if s[val] in seen:
                seen[s[val]] += 1
            else:
                seen[s[val]] = 1
        
        for val in range(len(t)):
            if t[val] in seen:
                seen[t[val]] -= 1
            else:
                return False

        for count in seen.values():
            if count != 0:
                return False
        return True

        