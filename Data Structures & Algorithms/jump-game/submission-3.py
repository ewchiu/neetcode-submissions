class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # set a goal at the end index
        # iterate through nums backwards starting from end - 1
        # at each index, check to see if it is possible to hit the goal from 
        # that index + the jump size
        # if so move the goalpost up

        # goal is leftmost index we can reach
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0