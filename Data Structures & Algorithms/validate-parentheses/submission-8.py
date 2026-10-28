class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # stack - go through the string, adding open brackets to the stack
        # if there is a close bracket in the string, pop the stack and check to make sure it's the correct char
        # if not return false
        # return true at the end
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
