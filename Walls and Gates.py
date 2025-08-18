class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """

        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        INF = 2147483647
        visited = [[False] * len(rooms[0]) for _ in range(len(rooms))]
        queue = deque()

        # Step 1: Add all gates (0s) to the queue
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    queue.append((row, col, 0))
                    visited[row][col] = True
        
        while queue:
            (row, col, length) = queue.popleft()

            for dirRow, dirCol in directions:
                nextRow = row + dirRow
                nextCol = col + dirCol
            
                # check bounds and if not visited and next spot is INF
                if (0 <= nextRow < len(rooms)
                and 0 <= nextCol < len(rooms[0]) and not visited[nextRow][nextCol] and rooms[nextRow][nextCol] == INF):
                    visited[nextRow][nextCol] = True
                    # next room is assigned 1 length more
                    rooms[nextRow][nextCol] = rooms[row][col] + 1
                    queue.append((nextRow, nextCol, length + 1))



