class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_amount = 0

        while left < right:
            # start one pointer on left one on right
            # calc formula at each step (j - i) * min(heights[i], heights[j])
            # check to see if it's greater than max_amount, if so replace
            # inc/dec pointer with lower height
            amount = (right - left) * min(heights[left], heights[right])
            max_amount = max(max_amount, amount)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_amount
