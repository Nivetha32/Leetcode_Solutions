import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
       od = n*n
       ev = n*(n+1)
       return math.gcd(od,ev)



