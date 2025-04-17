from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        cnt = collections.defaultdict(list)
        result = 0

        for i in range(len(nums)):
            cnt[nums[i]].append(i)

        for val in cnt.values():
            if len(val) > 1:
                for j in range(len(val) - 1):
                    for n in range(j + 1, len(val)):
                        if val[j] * val[n] % k == 0:
                            result += 1
        
        return result
