from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hash = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in hash:
                return i // 3 + 1
            else:
                hash.add(nums[i])
        return 0
