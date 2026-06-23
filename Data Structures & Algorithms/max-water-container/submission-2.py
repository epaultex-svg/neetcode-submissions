class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r = 0, len(heights) - 1

        res = 0

        while l < r:
            currLen = min(heights[l], heights[r])
            currWid = (l - r)
            currArea =  abs(currLen * (l - r))

            res = max(res, currArea)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res