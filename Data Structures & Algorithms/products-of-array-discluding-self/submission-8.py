class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev_prod = nums[0]
        cp = 0
        cp_nums = list(nums)
        nums[0] = 1
        for i in range(1,len(nums)):
            cp = nums[i]
            nums[i] = prev_prod

            prev_prod *= cp
        
        prev_prod = cp_nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1,-1):
            nums[i] *= prev_prod
            prev_prod *= cp_nums[i]
            
        return nums
