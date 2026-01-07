class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        spacesi = set(spaces)
        for i,val in enumerate(s):
            if i in spacesi:
                res.append(' ')
            res.append(val)
        return "".join(res)
