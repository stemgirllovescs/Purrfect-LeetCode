class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        result = []

        row = 0
        col = 0
        directionIndex = 0

        for _ in range(len(matrix) * len(matrix[0])):
            result.append(matrix[row][col])
            visited[row][col] = True

            newRow = row + directions[directionIndex][0]
            newCol = col + directions[directionIndex][1]

            # if valid and not visited before, safely change the row and col
            if (0 <= newRow < len(matrix) and 0 <= newCol < len(matrix[0]) and 
            not visited[newRow][newCol]):
                row = newRow
                col = newCol
            else:
                # readjust directionIndex and then row and index
                directionIndex = (directionIndex + 1) % 4
                row = row + directions[directionIndex][0]
                col = col + directions[directionIndex][1]
        return result


    # Time O(M * N)
    # Space O(M * N)