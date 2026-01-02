class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t = 0
        for i in range(len(points)-1):
            l = points[i]
            l1 = points[i+1]

            m = abs(l1[0]-l[0])
            n = abs(l1[1]-l[1])
            t+=max(m,n)
        return t
