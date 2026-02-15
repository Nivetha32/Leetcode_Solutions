class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        l = Counter(nums)
        c=0
        for k,v in l.items():
            if v==1:
                c+=k
        return c

