from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False

        target = sum(nums) // 2

        cache = {}

        def dfs(i, cur):
            if cur > target:
                return False
            elif cur == target:
                return True
            
            if i == len(nums):
                return cur == target
            
            if (i, cur) in cache:
                return cache[(i,cur)]
            
            cache[(i,cur)] = dfs(i+1, cur + nums[i]) or dfs(i+1, cur)
            return cache[(i,cur)]

        return dfs(0,0)
