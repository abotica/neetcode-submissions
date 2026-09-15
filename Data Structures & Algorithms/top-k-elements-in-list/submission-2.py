from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [] # min-heap

        for x in Counter(nums).items(): # (val, freq)

            if len(heap) >= k:
                freq = heap[0][0]
                if x[1] > freq:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (x[1], x[0]))
            elif len(heap) < k:
                heapq.heappush(heap, (x[1], x[0]))

        return [x[1] for x in heap]
                
            
