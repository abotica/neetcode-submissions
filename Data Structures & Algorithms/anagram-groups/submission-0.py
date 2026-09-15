from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for v in strs:
            key = tuple(sorted(Counter(v).items()))
            if key not in groups:
                groups[key] = []

            groups[key].append(v)
        
        return list(groups.values())
        