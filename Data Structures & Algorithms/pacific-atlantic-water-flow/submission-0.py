class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS,COLS = len(heights), len(heights[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
        def dfs(r,c,prev,oceans,visited):
            if heights[r][c] > prev or (r,c) in visited:
                return None
            
            visited.add((r,c))

            prev = heights[r][c]

            for dr,dc in directions:
                nr,nc = r+dr, c+dc

                if nr < 0 or nc < 0:
                    oceans.add("P")
                    continue
                if nr >= ROWS or nc >= COLS:
                    oceans.add("A")
                    continue
                if oceans == {"P","A"}:
                    return oceans

                if (0 <= nr < ROWS and 0 <= nc < COLS):
                    dfs(nr,nc,prev,oceans,visited)
            if oceans == {"P","A"}:
                    return oceans
            return oceans

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                oceans = dfs(r,c,float("inf"),set(),set())
                if oceans == {"P","A"}:
                    res.append([r,c])

        return res

            