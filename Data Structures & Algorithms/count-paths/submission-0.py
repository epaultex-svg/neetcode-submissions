class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # sub-problem = let ways(r,c) = number of ways towards trophy at index (r,c)

        memo = {}

        def dfs(r,c):
            # base cases: r or c out of range -> return
            # person at trophy - return 1
            if (r,c) in memo:
                return memo[(r,c)]
            if r >= m or c >= n:
                return 0
            if (r,c) == (m-1,n-1):
                return 1

            res = dfs(r+1,c) + dfs(r,c+1)

            memo[(r,c)] = res

            return res
        
        return dfs(0,0)

            

        