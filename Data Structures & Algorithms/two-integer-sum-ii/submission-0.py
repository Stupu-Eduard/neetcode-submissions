class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lIndex = 0
        rIndex = len(numbers) - 1

        while lIndex < rIndex:
            # Check if the sum is lower or higher than the target
            if numbers[lIndex] + numbers[rIndex] < target:
                lIndex += 1
                continue
            if numbers[lIndex] + numbers[rIndex] > target:
                rIndex -= 1
                continue
            else:
                return [lIndex + 1,rIndex + 1] 
            
