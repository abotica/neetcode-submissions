from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        most_frequent = [x[0] for x in sorted(Counter(nums).items(), key=lambda a : a[1], reverse=True)]

        return most_frequent[:k] 