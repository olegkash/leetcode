class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num10 = set()
        N = len(nums[0])

        for n in nums:
            num10.add(int(n, 2))

        for i in range(N + 1):
            if i not in num10:
                return "{:0>16b}".format(i)[-N:]
