class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        ct1 = {}
        ct2 = {}

        for c in range(len(s1)):
            print(c)
            ct1[s1[c]] = ct1.get(s1[c], 0) + 1
            ct2[s2[c]] = ct2.get(s2[c], 0) + 1

        print(ct1, ct2)
        if ct1 == ct2:
            return True

        for r in range(len(s1), len(s2)):
            right = s2[r]
            left = s2[l]
            ct2[right] = ct2.get(right, 0) + 1

            ct2[left] -= 1
            if ct2[left] == 0:
                del ct2[left]

            l += 1

            print(ct1, ct2)

            if ct1 == ct2:
                return True  

        return False


