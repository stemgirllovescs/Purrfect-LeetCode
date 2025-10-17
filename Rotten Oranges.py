class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # create a queue, add beginning node(s) to queue
        # go through the directions, pop the node, explore neighbor valid nodes, add neighbor
        # node to the queue
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        visited =[[False] * len(grid[0]) for _ in range(len(grid))]
        queue = deque()
        freshCount = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # append all 2s to the queue
                if grid[row][col] == 2:
                    queue.append((row, col, 0))
                    visited[row][col] = True
                elif grid[row][col] == 1:
                    freshCount += 1
        
        if freshCount == 0:
            return 0
                
        while queue:
            (row, col, length) = queue.popleft()
            for dirRow, dirCol in directions:
                neiRow = row + dirRow
                neiCol = col + dirCol

                # check bounds
                if 0 <= neiRow < len(grid) and 0 <= neiCol < len(grid[0]) and grid[neiRow][neiCol] == 1 and not visited[neiRow][neiCol]:
                    queue.append((neiRow, neiCol, length + 1))
                    freshCount -= 1
                    visited[neiRow][neiCol] = True


        if freshCount == 0:
            return length
        else:
            return -1