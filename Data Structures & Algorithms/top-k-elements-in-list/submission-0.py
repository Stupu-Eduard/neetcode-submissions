from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        h = []

        for num in nums:
            d[num] += 1
        
        for key,val in d.items():
            heapq.heappush(h,(val,key))

            if len(h) > k:
                heapq.heappop(h)            
        
        res = [item[1] for item in h]
        return res


        