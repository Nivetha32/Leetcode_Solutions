class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p=[]
        for i in range(0,len(s),2*k):
            m = s[i:i+k][::-1]
            n = s[i+k:i+2*k]
            p.append(m)
            p.append(n)

        return "".join(p)
        
