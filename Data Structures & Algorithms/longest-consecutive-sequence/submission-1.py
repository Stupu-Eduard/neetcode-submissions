class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0

        for num in num_set:
            if num - 1 not in num_set:
                curr_seq = 1
                while num + 1 in num_set:
                    curr_seq += 1
                    num += 1
                if max_seq < curr_seq:
                    max_seq = curr_seq
        return max_seq
