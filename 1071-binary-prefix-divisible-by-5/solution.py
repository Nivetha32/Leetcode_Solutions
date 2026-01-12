class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        k=""
        l=[]
        for i in nums:
            k= k+str(i)
            m = int(k,2)
            if m%5==0:
                l.append(True)
            else:
                l.append(False)
        return l
