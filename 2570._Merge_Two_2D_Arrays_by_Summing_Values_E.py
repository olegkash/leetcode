from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []
        i1, i2 = 0, 0

        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1][0] == nums2[i2][0]:
                result.append([nums1[i1][0], nums1[i1][1] + nums2[i2][1]])
                i1 += 1
                i2 += 1
            elif nums1[i1][0] < nums2[i2][0]:
                result.append([nums1[i1][0], nums1[i1][1]])
                i1 += 1
            elif nums1[i1][0] > nums2[i2][0]:
                result.append([nums2[i2][0], nums2[i2][1]])
                i2 += 1

        result.extend(nums1[i1:])
        result.extend(nums2[i2:])

        return result    
