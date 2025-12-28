class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum( 1 for r  in grid  for i in r if i<0)
