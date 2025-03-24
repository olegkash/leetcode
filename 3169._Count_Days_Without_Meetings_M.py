from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings_sorted = sorted(meetings)
        result = meetings_sorted[0][0] - 1
        end = meetings_sorted[0][1]
        for i in range(1, len(meetings_sorted)):
            if end < meetings_sorted[i][0]:
                result += meetings_sorted[i][0] - end - 1

            end = max(end, meetings_sorted[i][1])        
        result += days - end

        return result  
