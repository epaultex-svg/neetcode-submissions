class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        res = 0
        ct = [0] * 26

        for r in range(len(s)):

            rScore = ord(s[r]) - ord("A")
            ct[rScore] += 1

            while (r - l + 1) - max(ct) > k:
                lScore = ord(s[l]) - ord("A")
                ct[lScore] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res
