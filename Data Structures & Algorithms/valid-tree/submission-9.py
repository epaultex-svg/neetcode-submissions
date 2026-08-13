class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjMap = defaultdict(list)
        seen = set()

        for node,nbr in edges:
            adjMap[node].append(nbr)
            adjMap[nbr].append(node)

        def noCycle(node,prev):
            if node in seen:
                return False
            
            seen.add(node)

            for nbr in adjMap[node]:
                if nbr == prev:
                    continue
                if not noCycle(nbr, node):
                    return False
            
            return True

        res = noCycle(0, -1) and len(seen) == n



        return res





        
