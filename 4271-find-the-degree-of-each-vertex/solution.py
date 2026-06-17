class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        p=[]
        for i in matrix:
            c=0
            for j in i:
                if j==1:
                    c+=1
            p.append(c)
        return p
            
