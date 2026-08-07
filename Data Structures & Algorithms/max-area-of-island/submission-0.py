class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0,-1]]
        seen = set()
        res = 0

        def bfs(r, c):
            q = deque()
            seen.add((r, c))
            q.append((r, c))
            area = 1

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if ((0 <= nr < ROWS) and
                    (0 <= nc < COLS) and
                    grid[nr][nc] == 1 and
                    (nr, nc) not in seen):
                        area += 1
                        seen.add((nr, nc))
                        q.append((nr, nc))
                
            return area

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    area = bfs(r, c)
                    res = max(res, area)

        return res

