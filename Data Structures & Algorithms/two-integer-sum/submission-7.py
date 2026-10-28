class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = {}

        for i, num in enumerate(nums):
            if num in saved:
                return [saved[num], i]
            
            diff = target - num
            saved[diff] = i
        