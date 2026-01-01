class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        m=[]
        i = len(num)-1
        while i>=0 or k>0:
          if i>=0:
            k+=num[i]
            i-=1
          m.append(k%10)
          k//=10
        return m[::-1]
    
