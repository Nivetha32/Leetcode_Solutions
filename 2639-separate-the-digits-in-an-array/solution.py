class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        k=[]
        for i in range(0,len(nums)):
                n= nums[i]
                t=[]
                while n>0:
                    t.append(n%10)
                    n//=10
                k.extend(t[::-1])
        return k

