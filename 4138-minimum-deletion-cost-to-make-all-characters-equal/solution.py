class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        t = sum(cost)
        l={}
        for p in range(len(s)):
            l[s[p]]=l.get(s[p],0)+cost[p]
        return t-max(l.values())
                
