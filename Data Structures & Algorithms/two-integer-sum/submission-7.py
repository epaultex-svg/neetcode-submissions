class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        targetMap = {}

        for i in range(len(nums)):
            if nums[i] in targetMap:
                return [targetMap[nums[i]], i]
            targetMap[target - nums[i]] = i
        