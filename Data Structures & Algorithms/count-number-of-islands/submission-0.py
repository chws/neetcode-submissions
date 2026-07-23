class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            for dx, dy in direction:
                nx, ny = i + dx, j + dy
                dfs(nx, ny)
            return

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    # dfs
                    dfs(i, j)
                    count += 1
        return count
