from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i, j, result = 0, 0, 0
        for x in nums:
            result = max(result, j*x)
            j = max(i - x, j)
            i = max(i, x)
        return result
        
