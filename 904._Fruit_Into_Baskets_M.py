class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        d = {}
        result = 0

        for r in range(len(fruits)):
            if fruits[r] in d:
                d[fruits[r]] += 1
            else:
                d[fruits[r]] = 1

            while len(d) > 2 and l <= r:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
            
            result = max(result, (r - l + 1))

        return result
