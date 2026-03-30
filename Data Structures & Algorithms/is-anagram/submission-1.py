class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for val in range(len(s)):
            seen[s[val]] = seen.get(s[val], 0) + 1
        
        for val in range(len(t)):
            seen[t[val]] = seen.get(t[val], 0) - 1

        for count in seen.values():
            if count != 0:
                return False
        return True

        