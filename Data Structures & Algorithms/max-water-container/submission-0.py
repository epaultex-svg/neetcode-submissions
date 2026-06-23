class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        res = 0

        for i, a in enumerate(heights):
            for j, b in enumerate(heights):
                
                area = abs(min(a, b) * (j - i))

                res = max(area, res)
        return res

