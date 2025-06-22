from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        N = len(s)
        for i in range(0, N, k):
            if (i + k) > N:
                extra = (k - (N - i))
                cur = s[i:] + fill * extra
            else:
                cur = s[i:i+k]
            
            result.append(cur)
        
        return result
