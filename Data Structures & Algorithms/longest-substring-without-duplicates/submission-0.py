class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        longest = 0

        window = set()

        while r < len(s):

            if s[r] not in window:
                window.add(s[r])
                r += 1
                longest = max(longest, len(window))
            else:
                window.remove(s[l])
                l += 1
            
        return longest