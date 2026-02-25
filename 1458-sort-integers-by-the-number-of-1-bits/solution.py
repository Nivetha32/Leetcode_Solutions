class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        n=[]
        for i in arr:
            m =bin(i).count('1')
            n.append((m,i))
        n.sort()   
        r = [v for i, v in n]
        return r


        
