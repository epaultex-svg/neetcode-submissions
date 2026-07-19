class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         need = {}

         for i, num in enumerate(nums):
            
            if num in need and i != need[num][1]:
                return [need[num][1], i]
            
            diff = target - num
            
            need[diff] = (num, i)

