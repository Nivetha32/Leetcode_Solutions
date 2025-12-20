class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        k,l,m =[],[],[]
        for i in nums:
           if i%3==0:
               k.append(i)
           elif i%3==1:
               l.append(i)
           else:
               m.append(i)
        k.sort(reverse=True)
        l.sort(reverse=True)
        m.sort(reverse=True)

        b=0
        if len(k)>=3:
            b=max(b,k[0]+k[1]+k[2])
        if len(l)>=3:
            b=max(b,l[0]+l[1]+l[2])
        if len(m)>=3:
            b=max(b,m[0]+m[1]+m[2])
        if k and l and m:
            b=max(b,k[0]+l[0]+m[0])
        return b
        
