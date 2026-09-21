class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pref = nums[0]
        for i in range(1,len(nums)):
            res[i] = pref
            pref *= nums[i]

        suf = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            res[i] *= suf
            suf *= nums[i]


        return res