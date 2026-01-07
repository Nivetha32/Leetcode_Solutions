class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        k=0
        m=0
        n=0
        for i in moves:
            if i=='L':
                k+=1
            elif i=='R':
                m+=1
            elif i=='_':
                n+=1
        return abs(k-m)+n


