class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = defaultdict(list)
        seen = set()
        ct = 0

        for node,nbr in edges:
            adjList[node].append(nbr)
            adjList[nbr].append(node)

        def dfs(cur,prev):
            if cur in seen:
                return
            
            seen.add(cur)

            for nbr in adjList[cur]:
                if nbr != prev:
                    dfs(nbr,cur)

            return 1

        for i in range(n):
            if i not in seen:
                ct += dfs(i,-1)

        return ct



        
