class Solution:
    def digitSum(self, s: str, k: int) -> str:
      while len(s)>k:
        m=""
        for i in range(0,len(s),k):
            p = s[i:i+k]
            soi=0
            for i in p:
                soi+=int(i)
            m+=str(soi)
        s=m
      return s
    

