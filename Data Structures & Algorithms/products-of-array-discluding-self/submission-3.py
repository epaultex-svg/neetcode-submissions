class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        preProd = []
        prod = 1
        for num in nums:
            preProd.append(prod)
            prod *= num
        
        postProd = [0] * len(nums)
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            postProd[i] = prod
            prod *= nums[i]
        
        res = [preProd[i] * postProd[i] for i in range(len(nums))]

        return res
        
        