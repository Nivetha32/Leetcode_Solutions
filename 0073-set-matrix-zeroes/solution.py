class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        l1=[False]*n
        l2=[False]*m
        for r in range(0,n):
            for c in range(0,m):
                if matrix[r][c]==0:
                    l1[r]=True
                    l2[c]=True
        for r in range(0,n):
            for c in range(0,m):
                if l1[r] or l2[c]:
                    matrix[r][c]=0
        return matrix


        
