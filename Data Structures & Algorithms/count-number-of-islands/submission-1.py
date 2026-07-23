class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            grid[i][j] = '0'
            stack = [[i, j]]
            while stack:
                x, y = stack.pop()
                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        stack.append([nx, ny])
            return
                    

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    # dfs
                    dfs(i, j)
                    count += 1
        return count
