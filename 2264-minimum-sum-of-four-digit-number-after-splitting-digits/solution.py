class Solution:
    def minimumSum(self, num: int) -> int:
         deci = sorted(map(int, str(num)))
         return (deci[0] + deci[1]) * 10 + (deci[2] + deci[3])
