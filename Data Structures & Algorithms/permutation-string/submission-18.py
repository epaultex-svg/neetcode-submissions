class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = defaultdict(int)
        s2Map = defaultdict(int)
        l = 0

        for r in range(len(s1)):
            s1Map[s1[r]] = 1 + s1Map.get(s1[r],0)
            s2Map[s2[r]] = 1 + s2Map.get(s2[r],0)
        
        if s1Map == s2Map:
            return True
        
        for r in range(len(s1),len(s2)):
            s2Map[s2[l]] -= 1
            if s2Map[s2[l]] == 0:
                del s2Map[s2[l]]
            s2Map[s2[r]] = 1 + s2Map.get(s2[r],0)
            
            if s1Map == s2Map:
                return True
            l += 1
        
        return False


            

