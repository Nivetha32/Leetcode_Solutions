class Solution:
    def maxPower(self, s: str) -> int:
      if not s:
            return 0
      maxi=1
      k=1
      for i in range(1,len(s)):
        if s[i]==s[i-1]:
            k+=1
            maxi = max(k,maxi)
        else:
            k=1
      return maxi
      
        
