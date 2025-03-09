from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        result = 0
        left = 0

        for rigth in range(1, n + k - 1):
            if colors[rigth % n] == colors[(rigth - 1) % n]:
                left = rigth

            if rigth - left + 1 >= k:
                result += 1

        return result
