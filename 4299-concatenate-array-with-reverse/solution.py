class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        p=[]
        for i in nums[::-1]:
            p.append(i)
        return nums+p

