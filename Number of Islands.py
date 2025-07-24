class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 1s indicate land, 0's indicate water
        # we can run a dfs and count the number of islands
        def dfs(row, col):

            # Make sure we are in bounds and if the current spot is an island and
            # we have not visited it before
            if (0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1"
            and not visited[row][col]):
                # [0, -1], [0, 1], [-1, 0], [1, 0]
                visited[row][col] = True
                dfs(row, col - 1)
                dfs(row, col + 1)
                dfs(row - 1, col)
                dfs(row + 1, col)

        # Create a 2D array with all False's to check if we visited the grid
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        result = 0

        # Go through the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if we see an island or 1 and we've never visited it before
                if grid[row][col] == "1" and not visited[row][col]:
                    dfs(row, col)
                    result += 1
        

        return result

        # O(M * N) for runtime and space complexity
        # I have the habit of making a visited array to not touch the original grid,
        # but of course, we can flip the numbers as we remove the visited array
