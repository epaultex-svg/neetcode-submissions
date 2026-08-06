class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        need = {}

        for i in range(len(nums)):
            if nums[i] in need:
                idx1 = need[nums[i]][1]
                return [idx1, i]

            need[target - nums[i]] = (nums[i], i)

