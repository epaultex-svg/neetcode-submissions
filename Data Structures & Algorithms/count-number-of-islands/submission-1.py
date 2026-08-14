class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS,COLS = len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        seen = set()
        ct = 0
        q = deque()

        def bfs(r,c):
            q.append((r,c))
            seen.add((r,c))

            while q:
                r,c = q.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr,c+dc

                    if ((0 <= nr < ROWS) and
                    (0 <= nc < COLS) and
                    (grid[nr][nc] == "1") and
                    ((nr,nc) not in seen)):
                        seen.add((nr,nc))
                        q.append((nr,nc))
                
            return


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in seen and grid[r][c] == "1":
                    bfs(r,c)
                    ct += 1

        return ct

        
