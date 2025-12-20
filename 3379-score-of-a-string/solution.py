class Solution:
    def scoreOfString(self, s: str) -> int:
        k= []
        f=0
        for i in s:
          k.append(ord(i))
        for o in range(len(k)-1):
           f += abs(k[o]-k[o+1])
           print(f)
        return f
           
