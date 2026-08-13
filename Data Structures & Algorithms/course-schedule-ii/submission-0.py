class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {c: [] for c in range(numCourses)}
        visited,cycle = set(), set()
        output = []

        for crs,pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True

            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visited.add(crs)
            output.append(crs)
            return output

        for crs in preMap.keys():
            if not dfs(crs):
                return []
        
        return output

        