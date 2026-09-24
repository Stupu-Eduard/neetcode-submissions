class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxProd = 0

        while left < right:
            minHeight =  min(heights[left],heights[right])
            curProd = (right - left) * minHeight

            if curProd > maxProd:
                maxProd = curProd
            
            # We move to the next bar from left/right
            # that has the smallest bar between the two of them
            if minHeight == heights[left]:
                left += 1
            elif minHeight == heights[right]:
                right -= 1
        
        return maxProd