class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = {}

        def dfs(i):

            if i in dp:
                return dp[i]
            
            res = 1

            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    res = max(res,1 + dfs(j))
            
            dp[i] = res
            return res
        
        for i in range(len(nums)):
            dfs(i)

        return max(dp.values())


        
            

