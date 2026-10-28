class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp = list(nums)

        # initialize copy of nums array, as the max sum at each subarray starts with
        # element at each index

        # iterate through the array, either taking the max of the current value or the running sum

        # for i in range(1, len(nums)):
            # dp[i] = max(nums[i], nums[i] + dp[i - 1])

        # return max(dp)

        maxSub = nums[0]
        currSum = 0

        for num in nums:
            if currSum < 0:
                currSum = 0
            currSum += num
            maxSub = max(maxSub, currSum)

        return maxSub