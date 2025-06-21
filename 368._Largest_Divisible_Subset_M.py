from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [ [n] for n in nums ]

        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    tmp = [nums[i]] + dp[j]
                    if len(dp[i]) < len(tmp):
                        dp[i] = tmp
    
        dp.sort(key=lambda x: len(x))
        return dp[-1]

