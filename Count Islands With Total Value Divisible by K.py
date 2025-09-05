class Solution(object):
    def countIslands(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        # Solve by dfs

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def dfs(row, col):
            total = 0
            # make sure we're in bounds and on land and not visited before
            if (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0 and not visited[row][col]):
                visited[row][col] = True
                total = grid[row][col]

                total += dfs(row, col - 1)
                total += dfs(row, col + 1)
                total += dfs(row - 1, col)
                total += dfs(row + 1, col)
            return total

        result = 0
        # go through the whole grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0 and not visited[row][col]:
                    sumValue = dfs(row, col)
                    if sumValue % k == 0:
                        result += 1
        return result



        