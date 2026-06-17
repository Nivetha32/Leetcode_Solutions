class Solution:
    def processStr(self, s: str) -> str:
        res = ""
        for i in s:
            if i.islower():
                res+=i   
            elif i=='*':
                res = res[:-1]
              
            elif i=="#":
                res = res*2
               
            elif i=="%":
                res = res[::-1]
                
        return res                    

        
