class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1,max(piles)
        res = r

        while l <= r:
            t = 0
            mid = (l + r)//2
            for pile in piles:
                t += math.ceil(pile/mid)

            if t > h:
                l = mid + 1
            if t <= h:
                res = min(res, mid)
                r = mid - 1
            
            

        return res

