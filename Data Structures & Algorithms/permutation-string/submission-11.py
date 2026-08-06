class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        ct1 = dict(Counter(s1))
        ct2 = dict(Counter(s2[0:len(s1)]))
        l = 0

        if ct2 == ct1:
                return True
        
        for r in s2[len(s1):]:
            

            ct2[r] = 1 + ct2.get(r, 0)

            
            
            ct2[s2[l]] -= 1
            if ct2[s2[l]] == 0:
                del ct2[s2[l]]
            
            
            l += 1

            if ct2 == ct1:
                return True

        return False  
            
            







