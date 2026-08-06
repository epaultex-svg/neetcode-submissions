class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            score = [0] * 26
            for c in s:
                score[ord(c) - ord('a')] += 1

            res[tuple(score)].append(s)

        return list(res.values())