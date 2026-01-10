class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        k = bin(n)[2:]
        return "00" not in k and "11" not in k

