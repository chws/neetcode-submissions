class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # visit every island, and mark it with -1
        # update max value after every cycle

        max_area = 0
        n, m = len(grid), len(grid[0])
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        def dfs(i, j):
            grid[i][j] = -1
            stack = [[i, j]]
            area = 1
            while stack:
                x, y = stack.pop()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = -1
                        stack.append([nx, ny])
                        area += 1
            return area                

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    curr_area = dfs(i, j)
                    max_area = max(max_area, curr_area)
        return max_area