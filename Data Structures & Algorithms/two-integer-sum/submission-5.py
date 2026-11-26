class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i,num in enumerate(nums):
            if (target - num) in nums[i+1:]:
                j = nums[i+1:].index(target-num) + i + 1
                if i != j:
                    return [i,j]
        return -1