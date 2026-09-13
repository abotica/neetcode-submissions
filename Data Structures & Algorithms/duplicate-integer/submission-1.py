class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}

        for x in nums:
            counter[x] = counter.get(x, 0) + 1
            if counter[x] > 1:
                return True
        
        return False
        