class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = {}
        counter_t = {}

        for x in s:
            counter_s[x] = counter_s.get(x, 0) + 1
        
        for y in t:
            counter_t[y] = counter_t.get(y, 0) + 1

        if counter_s == counter_t:
            return True
        
        return False