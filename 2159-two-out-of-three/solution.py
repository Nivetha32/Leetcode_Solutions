class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        k = set(nums1)
        l = set(nums2)
        m = set(nums3)
        g = (k&l)| (l&m) | (m&k)
        return list(g)


