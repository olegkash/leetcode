from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        diff = [0] * N

        for l, r in queries:
            diff[l] += 1
            if r < N - 1:
                diff[r+1] -= 1

        for i in range(1, N):
            diff[i] += diff[i - 1]        

        for i in range(N):
            if nums[i] - diff[i] > 0:
                return False
        
        return True
