class Solution:
    def secondHighest(self, s: str) -> int:
        k=set()
        for i in s:
            if i.isdigit():
                k.add(int(i))
        m = list(sorted(k,reverse=False))
        if len(m)<2:
            return -1
        else:
            return m[-2]
        
