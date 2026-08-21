class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        nS = ""

        for c in s:
            if c.isalnum():
                nS += c

        l,r = 0,len(nS) - 1

        while l < r:
            while not nS[l].isalnum():
                l += 1
            while not nS[r].isalnum():
                r -= 1
            
            if not nS[l] == nS[r]:
                return False
            
            l += 1
            r -= 1
        return True