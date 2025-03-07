from typing import List
import heapq

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        result = []
        mindiff = float("inf")
        magic = [True] * (right + 1)
        magic[0] = magic[1] = False

        for i in range(2, right // 2 + 1):
            if magic[i]:
                for n in range(i * i, right+1, i):
                    magic[n] = False

        
        heapq.heapify(result)
        magic2 = []

        for i in range(left, right + 1):
            if magic[i]:
                magic2.append(i)
        
        for i in range(len(magic2) - 1):
            mindiff = min(mindiff, (magic2[i+1] - magic2[i]))
            heapq.heappush(result, (mindiff, [magic2[i], magic2[i+1]]) )

        if len(result) == 0:
            return [-1, -1]
    
        return heapq.heappop(result)[1]
