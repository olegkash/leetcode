from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = 0
        bigger = len(nums) - 1
        result = [0] * len(nums)

        for (num1, num2) in zip(nums, reversed(nums)):
            if num1 < pivot:
                result[smaller] = num1
                smaller += 1
            if num2 > pivot:
                result[bigger] = num2
                bigger -= 1
        
        while smaller <= bigger:
            result[smaller] = pivot
            smaller += 1

        return result 
