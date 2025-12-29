class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        p = str(n)
        l=[]
        k = Counter(p)
        m = min(k.values())
        for key,val in k.items():
            if val == m:
                l.append(int(key))
        return min(l)
           

        
