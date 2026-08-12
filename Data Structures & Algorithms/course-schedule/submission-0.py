class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        seen = set()
        for pre,crs in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            nonlocal seen
            if crs in seen:
                return False
            if preMap[crs] == []:
                return True
            seen.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            seen = set()
            preMap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

