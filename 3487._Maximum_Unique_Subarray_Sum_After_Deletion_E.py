class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unic = set(nums)
        result = 0
        max_n = float("-inf")

        for n in unic:
            max_n = max(n, max_n)
            if n > 0:
                result += n

        if result == 0:
            result = max_n
            
        return result
