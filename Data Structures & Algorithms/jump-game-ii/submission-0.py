class Solution:
    def jump(self, nums: List[int]) -> int:
        # brute force - start at index 0 and explore all paths from reachable indices from here
        # exponential time

        # greedy approach
        # 

        l, r = 0, 0
        result = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest
            result += 1
        
        return result