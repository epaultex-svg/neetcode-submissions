class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS,COLS = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        seen = set()
        res = 0

        def dfs(r,c):
            seen.add((r,c))
            area = 1

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if ((0 <= nr < ROWS) and
                (0 <= nc < COLS) and
                (grid[nr][nc] == 1) and
                ((nr,nc) not in seen)):
                    area += dfs(nr,nc)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) not in seen) and grid[r][c] == 1:
                    area = dfs(r,c)
                    res = max(res,area)
        return res