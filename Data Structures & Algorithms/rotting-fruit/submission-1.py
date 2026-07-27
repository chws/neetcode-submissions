from collections import deque
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # record the shortest distance to 2(rotten fruit)
        # so we need to do BFS
        # we'll record with negative number
        q = deque()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
        time = 0
        while q:
            x, y = q.popleft()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    if grid[x][y] == 2:
                        grid[nx][ny] = -1
                    elif grid[x][y] < 0:
                        grid[nx][ny] = grid[x][y] - 1
                    time = min(grid[nx][ny], time)
                    q.append((nx, ny))
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return time * (-1)
