from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS
        q = deque()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            x, y= q.popleft()
            dis = grid[x][y]
            # iterate neighbors and only put those into the queue 
            # when distance is larger than current dist+1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > dis + 1:
                    grid[nx][ny] = dis + 1
                    q.append((nx, ny))
        return
