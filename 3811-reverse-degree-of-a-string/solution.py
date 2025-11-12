class Solution:
    def reverseDegree(self, s: str) -> int:
        list=[]
        sum=0
        for i in s :
             b=ord(i)
             c= 122-b+1
             list.append(c)
        for ind, val in enumerate(list):
             sum+=((ind+1)*val)
        return sum

       # return sum((i+1)*26-(ord(val-97)) for i, val in enumerate(s))
