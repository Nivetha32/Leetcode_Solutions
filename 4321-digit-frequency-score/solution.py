class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        p = str(n)
        c=0
        l = Counter(p)
        for i, k in l.items():
                c+=int(i)*int(k)
        return c
