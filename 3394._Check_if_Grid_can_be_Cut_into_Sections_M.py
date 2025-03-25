from typing import List

class Solution:
    def cuts(self, rec):
        count = 0
        cur_end = -1
        for start, end in rec:
            if cur_end <= start:
                count += 1
            cur_end = max(cur_end, end)
        return count > 2

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = sorted([ [r[0],r[2]] for r in rectangles])
        y = sorted([ [r[1],r[3]] for r in rectangles])

        return self.cuts(x) or self.cuts(y)
