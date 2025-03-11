class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result = 0

        cnt = {
            "a": 0,
            "b": 0,
            "c": 0,
        }

        left = 0
        for r in range(len(s)):
            cnt[s[r]] += 1

            while cnt["a"] >= 1 and cnt["b"] >= 1 and cnt["c"] >= 1:
                result += len(s) - r
                cnt[s[left]] -= 1
                left += 1
        
        return result 
