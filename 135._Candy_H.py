from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n, ans = len(ratings), [1]*len(ratings)
        
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                ans[i+1] = max(1 + ans[i], ans[i+1])
                
        for i in range(n-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                ans[i] = max(1 + ans[i+1], ans[i])
        
        return sum(ans) 
