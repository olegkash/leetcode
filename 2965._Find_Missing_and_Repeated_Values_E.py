from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n ** 2

        cnt = [0] * (N + 1)

        for i in range(n):
            for j in range(n):
                cnt[grid[i][j]] += 1
        
        twice = 0
        missing = 0

        for i, num in enumerate(cnt):
            if num == 0:
                missing = i
            elif num == 2:
                twice = i

        return [twice, missing]
