class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        k= abs(x-z)
        m= abs(y-z)
        if k>m :
            return 2
        elif k<m:
            return 1
        else:
            return 0
