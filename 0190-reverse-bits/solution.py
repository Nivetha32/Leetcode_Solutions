class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        k = bin(n)[2:]
        k=k.zfill(32)
        return int(k[::-1],2)
   
