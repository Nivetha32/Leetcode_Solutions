class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        n=[]
        for i in range(len(mat)):
                c=0
                for j in mat[i]:
                    if j==1:
                        c+=1
                n.append([i,c])
        ma_p = max(n, key=lambda x: x[1])
        return ma_p
                



        
