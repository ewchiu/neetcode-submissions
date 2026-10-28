class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        # brute force - at every temperature in the arr, search for the next index that has a warmer temperature. add the difference in indexes to result
        # stack - 1. iterate through temp list
        # 2. while the stack is not empty and current temp > top of stack, pop the top element and compute how many days ahve passed
        # 3. push current day onto the stack
        # [2 1 1 3]
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
            stack.append((temp, i))

        return result