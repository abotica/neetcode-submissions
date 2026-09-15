class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, curr in enumerate(nums):
            needed = target - curr

            if needed in seen:
                return [seen[needed], i]
            
            seen[curr] = i