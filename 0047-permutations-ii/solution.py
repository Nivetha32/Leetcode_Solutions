class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        k = set(permutations(nums))
        return list(k)
