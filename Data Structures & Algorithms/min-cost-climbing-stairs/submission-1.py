class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        top = len(cost)
        cache = [-1] * len(cost)

        def dfs(i):
            if i >= top:
                return 0
            if cache[i] != -1:
                return cache[i]
            c = cost[i]
            cache[i] = c + min(dfs(i+1),dfs(i+2))
            return cache[i]
        
        return min(dfs(0),dfs(1))