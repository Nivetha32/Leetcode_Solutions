class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:  
        m = Counter(bulbs)
        p=[]
        for k,v in m.items():
            if v%2==1:
                p.append(k)
        return sorted(p)

