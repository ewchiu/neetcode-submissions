class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # iterate through nums backwards
        # at each index, see if it is possible to hit that index from the back

        # goal is leftmost index we can reach
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0