from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        result = 0
        left = 0

        for right in range(1, n + k - 1):
            if colors[right % n] == colors[(right - 1) % n]:
                left = right

            if right - left + 1 >= k:
                result += 1

        return result
