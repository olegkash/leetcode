from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0
        left = 0
        has_zero = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                has_zero += 1
            
            while has_zero > 1:
                if nums[left] == 0:
                    has_zero -= 1
                left += 1
            
            result = max(result, r - left)
        
        return result
