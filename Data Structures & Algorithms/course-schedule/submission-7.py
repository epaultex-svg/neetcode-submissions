class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = defaultdict(list)
        seen = set()

        for pre in prerequisites:
            preMap[pre[1]].append(pre[0])



        def dfs(node):

            if preMap[node] == []:
                return True
            if node in seen:
                return False
            
            seen.add(node)

            for crs in preMap[node]:
                if not dfs(crs):
                    return False

            seen.remove(node)
            preMap[node] = []
            return True

        for pre in prerequisites:
            if not dfs(pre[0]):
                return False
        return True