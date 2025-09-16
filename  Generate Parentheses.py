from shutil import register_unpack_format


class Solution(object):
    def generateParenthesis(self, n):
        # We use stack and backtracking for this problem
        stack = []
        result = []
        def backtrack(openCount, closedCount):
            # Base case: when openCount and closedCount and n are the same,
            # no more left
            if (openCount == closedCount == n):
                result.append("".join(stack))
                return
            
            # if we don't have all openCounts
            if openCount < n:
                # Add ( to stack, backtrack, undo
                stack.append("(")
                backtrack(openCount + 1, closedCount)
                stack.pop()

            # if we don't have all closedCounts in a way that 
            # we cannot close more than we opened
            if closedCount < openCount:
                # Add ) to stack, backtrack, undo
                stack.append(")")
                backtrack(openCount, closedCount + 1)
                stack.pop()

        backtrack(0, 0)
        return result
        # Space: O(N)
        # Time: O(4^N/Sqrt(N))