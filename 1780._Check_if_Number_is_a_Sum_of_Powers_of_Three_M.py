class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        stack = []
        result = 0
        p = 1

        while p <= n:
            stack.append(p)
            p *= 3

        while stack:
            cur = stack.pop()

            if cur <= n - result:
                result += cur
        
        return result == n 
