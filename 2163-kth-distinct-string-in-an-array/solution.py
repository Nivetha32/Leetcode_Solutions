class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        m = Counter(arr)
        p=[]
        for ki , v in m.items():
            if v==1:
                p.append(ki)
        if k<=len(p):
          return p[k-1]
        return ""
        
        
               
        
        



