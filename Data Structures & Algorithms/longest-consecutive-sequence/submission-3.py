class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_length = 0

        for n in nums:
            length = 1
            if n - 1 in numSet:
                continue
            while n + length in numSet:
                length += 1
            max_length = max(length,max_length)
        
        return max_length