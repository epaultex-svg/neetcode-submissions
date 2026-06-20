class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        numset = set(nums)
        res = 0
        longest = 0
        j = 1
        for i in range(len(nums)):
            if not nums[i] - 1 in numset:
                
                while nums[i] + j in numset:
                    longest += 1
                    j += 1
            res = max(res, longest)
            j = 1
            longest = 0
        return res + 1