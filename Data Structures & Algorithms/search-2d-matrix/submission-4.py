class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        r_lo, r_hi = 0, len(matrix[0]) - 1

        if target < matrix[0][0]:
            return False

        while lo <= hi:
            mid = (lo + hi) // 2
            if target > matrix[mid][0] and (mid + 1 == len(matrix) or target < matrix[mid + 1][0]):

                while r_lo <= r_hi:
                    r_mid = (r_lo + r_hi) // 2
                    if target > matrix[mid][r_mid]:
                        r_lo = r_mid + 1
                    elif target < matrix[mid][r_mid]:
                        r_hi = r_mid - 1
                    else:
                        return True
                return False

            if target > matrix[mid][0]:
                lo = mid + 1
            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                return True
        return False