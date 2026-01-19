class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        k=[]
        m=[]
        for i in nums:
            if i%2==0:
                k.append(i)
            else:
                m.append(i)
        return k+m
