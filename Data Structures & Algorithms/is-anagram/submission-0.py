class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def getFrequency(string: str) -> {}:
            frequency = {}

            for c in string:
                frequency[c] = frequency.get(c, 0) + 1
            return frequency

        if getFrequency(s) == getFrequency(t):
            return True
        
        return False
