class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS,COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
    
        q = deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))

        minutes = 0
        while q:
            if fresh == 0:
                break
            
            qlen = len(q)

            for _ in range(qlen):
                r,c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc

                    if (0 <= nr < ROWS and
                    0 <= nc < COLS and
                    grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
            minutes += 1        
            

        if fresh == 0:
            return minutes
        return -1
                


                

                    