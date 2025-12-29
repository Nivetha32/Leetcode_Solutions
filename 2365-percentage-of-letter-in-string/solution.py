class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        k = len(s)
        c=0
        for i in s:
          if i==letter:
            c+=1
        return int(c/k*100)
        

      
           


        
