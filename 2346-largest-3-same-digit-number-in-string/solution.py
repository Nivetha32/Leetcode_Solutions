class Solution:
    def largestGoodInteger(self, num: str) -> str:
        g = ""
        for i in range(len(num)-2):
             if num[i]==num[i+1]==num[i+2]:
                m = num[i]*3
                if m>g:
                    g=m
        return g
