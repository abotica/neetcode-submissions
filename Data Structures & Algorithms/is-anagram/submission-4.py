class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}

        if len(s) != len(t):
            return False

        for i, x in enumerate(s):
            counter[x] = counter.get(x, 0) + 1
            counter[t[i]] = counter.get(t[i], 0) - 1

        return all(x == 0 for x in counter.values())
        
        
        
            