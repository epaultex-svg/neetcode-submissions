class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anaMap = defaultdict(list)

        for s in strs:
            candidate = tuple(sorted(s))
            
            anaMap[candidate].append(s)
        
        res = []
        for val in anaMap.values():
            res.append(val)
        
        return res
        