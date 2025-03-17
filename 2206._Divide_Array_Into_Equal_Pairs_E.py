from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash = set()

        for n in nums:
            if n in hash:
                hash.remove(n)
            else:
                hash.add(n)
        
        return not hash
