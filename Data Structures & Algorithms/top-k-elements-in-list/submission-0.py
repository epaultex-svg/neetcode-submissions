class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        most_freq = list(sorted(count, key=count.get, reverse=True)) or []

        print(most_freq)

        return most_freq[0:k]