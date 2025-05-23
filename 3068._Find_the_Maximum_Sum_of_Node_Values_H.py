from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        result = sum(nums)

        delta = [(num ^ k) - num for num in nums]        
        delta.sort(reverse=True)

        n = len(delta)
        if n % 2 == 1:
            n -= 1
        for i in range(0,n-1,2):
            sum_pair = delta[i] + delta[i+1]
            if sum_pair > 0:
                result += sum_pair
        
        return result 
