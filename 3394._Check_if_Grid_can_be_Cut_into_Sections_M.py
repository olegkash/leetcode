from typing import List

class Solution:
    def cuts(self, rec):
        result = 0
        cur_end = rec[0][1]
        for i in range(1, len(rec)):
            if cur_end <= rec[i][0]:
                result += 1
            cur_end = max(cur_end, rec[i][0], rec[i][1])
        return result > 1

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        vert = []
        hor = []

        for xs, ys, xe, ye in rectangles:
            vert.append([ys,ye])
            hor.append([xs, xe])

        vert.sort()
        hor.sort()

        return self.cuts(vert) or self.cuts(hor)
