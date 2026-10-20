class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        l = 0
        r = 1

        if len(prices) == 1:
            return 0
        
        while r < len(prices):
            max_sum = max(max_sum,prices[r] - prices[l])

            if prices[l] >= prices[r]:
                l = r
            
            r += 1

        return max_sum

            