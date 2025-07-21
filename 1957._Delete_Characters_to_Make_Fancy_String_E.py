class Solution:
    def makeFancyString(self, s: str) -> str:

        result = []

        prev = s[0]
        count = 0
        for r, c in enumerate(s):
            if c == prev:
                count += 1
                if count > 2:
                    continue
                
            else:
                prev = c
                count = 1
            
            result.append(c)

        return "".join(result)
