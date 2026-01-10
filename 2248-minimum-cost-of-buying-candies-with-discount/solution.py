class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        k=0
        for i in range(0,len(cost)):
            if i%3!=2:
                k+=cost[i]
        return k





