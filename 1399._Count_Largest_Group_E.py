class Solution:
    def countLargestGroup(self, n: int) -> int:
        max_cnt = float("-inf")
        cnt = collections.defaultdict(int)

        for i in range(1, n + 1):
            tmp = 0
            while i:
                tmp += i % 10
                i //= 10
            
            cnt[tmp] += 1
            max_cnt = max(max_cnt, cnt[tmp])

        result = 0
        for val in cnt.values():
            if val == max_cnt:
                result +=1

        return result
