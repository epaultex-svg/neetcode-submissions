class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        presum = 0
        res, sol = [], []

        def backtrack(i,sol, presum):
            if presum == target:
 
                res.append(sol[:])
                return
            elif presum > target or i == len(nums):
                
                sol = []
                return
            
    
            presum += nums[i]
            sol.append(nums[i])
            backtrack(i, sol, presum)

            sol.pop()
            presum -= nums[i]
            backtrack(i+1, sol, presum)

        backtrack(0, [], presum)
            
        return res


                
        