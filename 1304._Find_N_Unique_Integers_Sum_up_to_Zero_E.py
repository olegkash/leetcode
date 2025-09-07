class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2:
            result.append(0)
            n -= 1
        
        for i in range(n//2):
            num = i + 1
            result.append(num)
            result.append(-num)
        
        return result
