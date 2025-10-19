class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        # Gravity
        # We have a lowest empty col at the end of the box of each row
        for row in range(len(boxGrid)):
            lowestEmptyCol = len(boxGrid[0]) - 1
            for col in reversed(range(len(boxGrid[0]))):
                # if we have an obstacle, then the lowest col is on the left of the current element
                if boxGrid[row][col] == "*":
                    lowestEmptyCol = col - 1
                elif boxGrid[row][col] == "#":
                    # if we have a stone, and the current col != lowest empty col, then safely swap by mark current spot as .
                    # and also the position of the lowest empty col as #. 
                    if col != lowestEmptyCol:
                        boxGrid[row][col] = "."
                        boxGrid[row][lowestEmptyCol] = "#"
                    lowestEmptyCol -= 1

        # Actual Rotation
        # we make a new 2D array to be called result
        result = []
        # remember now it's col, then reversed row because visually, 
        # [A, B, C],
        # [D, E, F]
        # Becomes
#         [D, A],
#         [E, B],
#         [F, C]
        for col in range(len(boxGrid[0])):
            newRow = []
            for row in reversed(range(len(boxGrid))):
                newRow.append(boxGrid[row][col])
            result.append(newRow)
        
        return result

        # Time: O(m * n)
        # Space: O(m * n) (for the result grid)
        # reviewed today


 