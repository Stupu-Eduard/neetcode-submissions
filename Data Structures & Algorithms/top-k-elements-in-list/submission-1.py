class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        res = []
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            d1[num] = d1.get(num,0) + 1
        
        for num,count in d1.items():
            buckets[count].append(num)

        for i in range(len(buckets) - 1,0,-1):
            for val in buckets[i]:
                if len(res) < k:
                    res.append(val)
                else:
                    return res
        return res