class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       k = Counter(nums)
       for key , val in k.items():
            if val ==1:
                return key

