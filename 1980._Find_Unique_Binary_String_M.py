class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0])

        num10 = { int(n, 2) for n in nums }

        for i in range(N + 1):
            if i not in num10:
                return "{:0>16b}".format(i)[-N:]
