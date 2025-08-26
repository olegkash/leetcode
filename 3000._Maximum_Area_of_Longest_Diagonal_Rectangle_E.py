from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        max_area = 0

        for x, y in dimensions:
            cur_diag = x*x + y*y
            if cur_diag > max_diag:
                max_area = x * y
                max_diag = cur_diag
            elif cur_diag == max_diag:
                max_area = max(max_area, x * y)

        return max_area
