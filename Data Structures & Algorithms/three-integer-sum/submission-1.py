class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cIndex = 0

        res = []
        nums.sort()

        while cIndex < len(nums):
            lIndex = 0
            rIndex = len(nums) - 1

            while lIndex < rIndex:

                # If lIndex or rIndex are the same as cIndex
                # add one to lIndex or substract one from rIndex
                if cIndex == lIndex:
                    lIndex += 1
                    continue

                if cIndex == rIndex:
                    rIndex -= 1
                    continue

                # If the sum is bigger than the desired number, substract 1 from rIndex
                if nums[lIndex] + nums[rIndex] > -nums[cIndex]:
                    rIndex -= 1
                    continue
                
                if nums[lIndex] + nums[rIndex] < -nums[cIndex]:
                    lIndex += 1
                    continue
                
                if nums[lIndex] + nums[rIndex] == -nums[cIndex]:
                    sublist = [nums[lIndex],nums[rIndex],nums[cIndex]]
                    if sorted(sublist) not in res:
                        res.append(sorted(sublist))

                    lIndex += 1
                    rIndex -= 1

            cIndex += 1
        
        return res

          
