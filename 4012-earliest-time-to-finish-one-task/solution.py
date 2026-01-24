class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        k=[]
        for i in tasks:
           k.append(i[0]+i[1])
        return min(k)
