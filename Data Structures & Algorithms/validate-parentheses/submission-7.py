class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = ['(', '[', '{']

        # stack - go through the string, adding open brackets to the stack
        # if there is a close bracket in the string, pop the stack and check to make sure it's the correct char
        # if not return false
        # return true at the end
        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()
                if char == ')' and last_open == '(':
                    continue
                elif char == ']' and last_open == '[':
                    continue
                elif char == '}' and last_open == '{':
                    continue
                else:
                    return False
        return len(stack) == 0
