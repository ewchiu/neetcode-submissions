class Solution:
    def isValid(self, s: str) -> bool:
        # brute force - whenever you come upon an open bracket, search the rest of the string to make sure it's closed

        # stack - go through the string, adding open brackets to the stack
        # if there is a close bracket in the string, pop the stack and check to make sure it's the correct char
        # if not return false
        # return true at the end
        stack = []
        open_brackets = ['(', '[', '{']

        for char in s:
            if char in open_brackets:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last_open = stack.pop()

                if last_open == '(' and char != ')':
                    return False
                elif last_open == '{' and char != '}':
                    return False
                elif last_open == '[' and char != ']':
                    return False
        
        return len(stack) == 0
