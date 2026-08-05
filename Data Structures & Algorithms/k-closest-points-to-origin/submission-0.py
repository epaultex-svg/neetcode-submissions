class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []

        for point in points:
            distance = math.sqrt((point[0]**2) + (point[1]**2))

            print((point[0], point[1]))

            print((distance, point))

            heapq.heappush(minheap, (distance, point))

        res = []

        for _ in range(k):
            pd = heapq.heappop(minheap)

            res.append(pd[1])

        return res

        

