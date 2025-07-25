class Solution(object):
    def minimumOperationsToWriteY(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Start with a large value as our result, and we minimize as we go
        result = len(grid) * len(grid)

        center = len(grid) // 2

        # We have distinct y values and bg values that are not identical
        # 0, 1, 2
        for y in range(3):
            for bg in range(3):
                # y and bg values should be distinct, so we skip them if identical
                if y == bg:
                    continue

                # Now we keep track of changes in y or bg values as we go through the grid
                changes = 0
                for row in range(len(grid)):
                    for col in range(len(grid[0])):
                        # if it's part of the y structure but different from y,
                        # increment change
                        # [0, 0] [0, 1] [0, 2]
                        # [1, 0] [1, 1] [1, 2]
                        # [2, 0] [2, 1] [2, 2]
                        isDiagonal = ((row == col) or (row + col == len(grid) - 1)) and row <= center
                        isVertical = (col == center) and row >= center
                        if isDiagonal or isVertical:
                            # if we're part of the y structure
                            if grid[row][col] != y:
                                changes += 1
                        else:
                        # if it's part of bg, but different from bg, increment change
                            if grid[row][col] != bg:
                                changes += 1
                # run through the whole grid and then update the result
                result = min(result, changes)

        return result
        # O(N^2) runtime
        # O(1) space
