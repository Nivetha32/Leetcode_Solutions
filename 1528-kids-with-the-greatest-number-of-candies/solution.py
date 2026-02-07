class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=[]
        m = True
        n = False
        k = max(candies)
        for i in range(0,len(candies)):
            if candies[i]+extraCandies >=k:
                l.append(m)
            else:
                l.append(n)
        return l


