class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution using a Min-Heap
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        #  count = {num : frequency}

        # Initializing a heap (priority-queue)
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            # heap = {freq, num}
            if len(heap) > k:
                heapq.heappop(heap)
            # popping all the elements that are with low frequency
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res