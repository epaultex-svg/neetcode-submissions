class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROWS,COLS = len(board),len(board[0])

        rD = defaultdict(set)
        cD = defaultdict(set)
        subD = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if not val.isnumeric():
                    continue
                
                
                if (val in rD[r]) or (val in cD[c]) or (val in subD[(r//3,c//3)]):
                    return False
                
                rD[r].add(val)
                cD[c].add(val)
                subD[(r//3,c//3)].add(val)
        
        return True

