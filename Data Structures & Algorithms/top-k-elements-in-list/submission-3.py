class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numCt = dict(Counter(nums))

        heap = []
        for num,ct in numCt.items():
            heapq.heappush(heap,(ct,num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [heapq.heappop(heap)[1] for i in range(len(heap))]

        

        



            

        