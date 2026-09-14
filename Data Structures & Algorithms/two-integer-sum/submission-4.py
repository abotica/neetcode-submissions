class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target = x + y
        # pass through an array, but remember what was seen, find out if needed value exist in there

        # needed = target - curr
        seen = {}

        for i, curr in enumerate(nums):
            needed = target - curr

            if needed in seen:
                return [seen[needed], i]

            seen[curr] = i
        
        return []



             