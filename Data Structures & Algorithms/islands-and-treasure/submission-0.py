class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        zeros = []

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c,0))

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        while q:
            
            qlen = len(q)

            for _ in range(qlen):
                r,c,dist = q.popleft()

                for dr,dc in directions:
                    nr,nc = r+dr, c+dc

                    if ((nr and nc) not in seen
                    and (0 <= nr < ROWS)
                    and (0 <= nc < COLS)
                    and grid[nr][nc] == 2147483647):
                        
                        grid[nr][nc] = dist + 1
                        seen.add((nr,nc))
                        q.append((nr,nc,dist + 1))


        
                



