class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for val in nums:
            counter[val] = counter.get(val, 0) + 1
            if counter[val] > 1:
                return True
        return False