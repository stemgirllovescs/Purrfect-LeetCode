from collections import deque


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visited = [[False] * len(rooms[0]) for _ in range(len(rooms))]
        INF = 2147483647
        queue = deque()

        # Add all the 0s, aka gates to the queue, because of multi source
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    queue.append((row, col, 0))
                    visited[row][col] = True

        while queue:
            (row, col, length) = queue.popleft()
            for dirRow, dirCol in directions:
                nextRow = dirRow + row
                nextCol = dirCol + col

                # check nextRow,nextCol are in bounds, not visited, and are INF(empty)
                if (0 <= nextRow < len(rooms) and 0 <= nextCol < len(rooms[0]) 
                and not visited[nextRow][nextCol] and rooms[nextRow][nextCol] == INF):
                    visited[nextRow][nextCol] = True
                    rooms[nextRow][nextCol] = rooms[row][col] + 1
                    queue.append((nextRow, nextCol, length + 1))
# Time Complexity: O(m × n)

# Space Complexity: O(m × n)