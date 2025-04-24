from typing import List
import collections

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        disct = len(set(nums))
        N = len(nums)
        result = 0
        cur = set()
        n = collections.defaultdict(int)
        left = 0

        for i in range(N):
            n[nums[i]] += 1
            cur.add(nums[i])

            while disct == len(cur):
                result += N - i
                n[nums[left]] -= 1
                if n[nums[left]] == 0:
                    cur.remove(nums[left])
                left += 1
                
        return result
