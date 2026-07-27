from collections import deque
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # record the shortest distance to 2(rotten fruit)
        # so we need to do BFS
        # we'll record with negative number
        q = deque()
        n, m = len(grid), len(grid[0])
        # optimize - keep 'fresh' to keep the count of 1
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        time = 0
        # optimize: we need fresh > 0 because in case it's not reachable it'll go to while loop again which makes time + 1
        while q and fresh > 0:
            time += 1
            # optimize: traverse the ones in the current time only
            # then we only need to update the cells into 2 (rotten)
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in DIRS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            
        return -1 if fresh > 0 else time
