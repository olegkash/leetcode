from typing import List

class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        meetings.sort()

        prev_end = 0

        for start, end in meetings:
            start = max(prev_end + 1, start)
            length = end - start + 1
            days -= max(length, 0)
            prev_end = max(prev_end, end)

        return days
