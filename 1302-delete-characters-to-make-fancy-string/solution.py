class Solution:
    def makeFancyString(self, s: str) -> str:
        k=[]
        for i in s:
            if len(k)>=2 and k[-1] == k[-2]== i :
                continue
            k.append(i)
        return "".join(k)
