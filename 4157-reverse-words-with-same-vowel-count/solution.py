class Solution:
    def reverseWords(self, s: str) -> str:
        vo="aeiou"
        wor = s.split()
        t = sum(ch in vo for ch in wor[0])
       
        for i in range(1,len(wor)):
            if sum(ch in vo for ch in wor[i])==t:
                wor[i]=wor[i][::-1]
        return " ".join(wor)
        
