class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {"}" : "{", "]" : "[", ")" : "("}
        for char in s:
            # if it's a closed bracket
            if char in closeToOpen:
                # if we have a stack and top of stack is a matching open parenthesis
                if stack and stack[-1] == closeToOpen[char]:
                    # safely pop it
                    stack.pop()
                else:
                    # mismatch, so return False early
                    return False
            else:
                # it's an open parenthesis
                stack.append(char)
        
        return not stack
    # Time O(N) Space = O(N)