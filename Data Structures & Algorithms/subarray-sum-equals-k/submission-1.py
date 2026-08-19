class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        preMap = {0:1}
        curSum = 0

        for num in nums:

            curSum += num
            diff = curSum - k

            res += preMap.get(diff,0)
            preMap[curSum] = 1 + preMap.get(curSum,0)

        return res