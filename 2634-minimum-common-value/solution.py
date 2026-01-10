class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
     m = set(nums1)& set(nums2)
     if not m:
        return -1
     else:
        return min(m)

