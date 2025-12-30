class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            if i%2==0:
                l.append("0")
            if i%2!=0:
                l.append("1")
        m = sorted(l,reverse=False)
        return [int(i) for i in m]

        
