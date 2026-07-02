class Solution:
    def search(self, nums, target, offset=0):
        if not nums:
            return -1
        mid = len(nums) // 2
        num = nums[mid]
        if num == target:
            return offset + mid
        elif num > target:
            return self.search(nums[:mid], target, offset)
        else:
            return self.search(nums[mid+1:], target, offset + mid + 1)