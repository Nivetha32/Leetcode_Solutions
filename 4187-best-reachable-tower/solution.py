class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        i,j = center
        e = -1
        s=[-1,-1]

        for a,b,c in towers:
             m = abs(a-i)+abs(b-j)

             if m<=radius:
               if c>e:
                   e=c
                   s=[a,b]
               elif c==e:
                   if s==[-1,-1] or (a< s[0] or (a ==s[0] and b < s[1])):
                       s=[a,b]
        return s
