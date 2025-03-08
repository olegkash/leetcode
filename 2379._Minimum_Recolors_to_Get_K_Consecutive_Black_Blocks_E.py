class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = k
        cur_W = 0

        left = 0
        for i in range(len(blocks)):
            if blocks[i] == "W":
                cur_W += 1
 
            if i - left + 1 == k:
                result = min(result, cur_W)
                if blocks[left] == "W":
                    cur_W -= 1
                left += 1

        return result
