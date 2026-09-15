class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # state: (i,amount left)

        dp = {}

        def dfs(i,amt):
            if amt == 0:
                return 1
            if i >= len(coins) or amt < 0:
                return 0
            if (i,amt) in dp:
                return dp[(i,amt)]
            
            
            res = dfs(i,amt - coins[i]) + dfs(i+1,amt)
            
            dp[(i,amt)] = res

            return res
        return dfs(0,amount)
        