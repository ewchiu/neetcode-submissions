from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0":
                    continue
                grid[row][col] = "0"
                q.append((row + 1, col))
                q.append((row - 1, col))
                q.append((row, col + 1))
                q.append((row, col - 1))
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands
        