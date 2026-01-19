class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        m=[]
        p=[]
        for i in nums:
            if i>0:
                m.append(i)
            else:
                p.append(i)
        l=[]
        min_l = min(len(m), len(p))
        for i in range(min_l):
            l.append(m[i])
            l.append(p[i])
        if len(m)>min_l:
           l.extend(m[min_l:])
        if len(p)>min_l:
            l.extend(p[min_l:])
        return l
        

