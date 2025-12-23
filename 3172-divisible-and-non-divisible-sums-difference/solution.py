class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = sum(i for i in range(1,n+1) if i%m!=0)
        y = sum(i for i in range(1,n+1) if i%m==0)
        return k-y

