from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        max_num = max(nums)
        count_max = 0
        N = len(nums)
        left = 0

        for r in range(N):
            if nums[r] == max_num:
                count_max += 1
            
            while count_max == k:
                result += (N - r)
                if nums[left] == max_num:
                    count_max -= 1
                left += 1

        return result
