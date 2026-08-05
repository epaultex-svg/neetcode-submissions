class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for i in stones:
            heapq.heappush(maxheap, -i)

        while len(maxheap) > 1:

            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)

            if x == y:
                continue
            elif y < x:
                heapq.heappush(maxheap, -(x - y))


        return -maxheap[0] if len(maxheap) > 0 else 0
        