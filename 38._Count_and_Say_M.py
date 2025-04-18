class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        def pairs(s):
            last = s[0]
            cnt = 1
            res = []

            for i in range(1, len(s)):
                if s[i] != last:
                    res.append([int(last), cnt])
                    last = s[i]
                    cnt = 1
                else:
                    cnt += 1
            
            res.append([int(last), cnt])
            return res

        def comb(l):
            result = ""
            for n, cnt in l:
                result += str(cnt) + str(n)
            
            return result

        for _ in range(n - 1):
            p1 = pairs(result)
            result = comb(p1)

        return result        
