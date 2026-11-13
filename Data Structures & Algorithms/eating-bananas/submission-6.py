class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)

        while lo <= hi:
            mid = (lo + hi) // 2
            count = sum((pile + mid - 1) // mid for pile in piles)

            if count <= h:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo