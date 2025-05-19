class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a = nums[0]
        b = nums[1]
        c = nums[2]

        if c >= a + b:
            return "none"

        if a == b == c:
            return "equilateral"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"
