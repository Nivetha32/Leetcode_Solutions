class Solution:
    def minLength(self, s: str) -> int:
        si=[]
        for ch in s:
            if si and ch =="B" and si[-1]=="A":
                si.pop()
            elif si and ch=="D" and si[-1]=="C":
                si.pop()
            else:
                si.append(ch)
        return len(si)
