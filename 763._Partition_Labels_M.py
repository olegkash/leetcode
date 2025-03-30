import collections
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = collections.defaultdict(int)

        for i, c in enumerate(s):
            last[c] = i
        
        end = 0
        size = 0
        result = []

        for i, c in enumerate(s):
            end = max(end, last[c])
            size += 1

            if i == end:
                result.append(size)
                size = 0

        return result
