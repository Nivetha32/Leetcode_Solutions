class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k%2 == 0 or k%5==0:
            return -1
        e =0
        f = set()

        for l in range(1,k+1):
            e = (e*10+1)%k
            if e ==0:
                return l
            if e in f:
                return -1
            f.add(e)
        return -1
