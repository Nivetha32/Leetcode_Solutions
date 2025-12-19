class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        o = {}
        for p in paths:
            a,b = p
            o[a]=o.get(a,0)+1
            o[b]=o.get(b,0)
        for i in o:
            if o[i]==0:
               return i

        
