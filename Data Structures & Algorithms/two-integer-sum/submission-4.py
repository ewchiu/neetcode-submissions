class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[n] = i

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([1, 2, 3], 4))