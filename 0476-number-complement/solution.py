class Solution:
    def findComplement(self, num: int) -> int:
        k = bin(num)
        m = k[2:]
        s=""
        for i in m:
            s+='0' if i=='1' else '1'
        return int(s,2)
