class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=[]
        for ch in s.split():
                if ch.isdigit():
                    l.append(int(ch))
        for i in range(len(l)-1):
            if(l[i]>=l[i+1]):
               return False
        return True

        
