class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        dis = []

        for point in points:
            d = point[0]**2 + point[1]**2

            dis.append((d, point))

        heapq.heapify(dis)

        res = [point for d, point in heapq.nsmallest(k, dis)]

        return res