class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                d = i
                break

        for i in range(n):
            if colors[i] != colors[n - 1]:
                d1= n - 1 - i
                break

        return max(d, d1)

            
