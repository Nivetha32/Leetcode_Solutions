class Solution:
    def maxProduct(self, n: int) -> int:
      k = []
      l = str(n)
      for i in range(0,len(l)):
         k.append(int(l[i]))
      k.sort()
      return k[-1]*k[-2]


