class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        k, l = edges[0]
        m, n = edges[1]

        if k==m or k==n:
            return k
        return l


                

        
        

            
