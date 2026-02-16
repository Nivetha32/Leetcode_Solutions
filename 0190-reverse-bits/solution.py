class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        m = bin(n)[2:]
        p = m.zfill(32)
        l = str(p)[::-1]
        return int(l,2)
    
   
