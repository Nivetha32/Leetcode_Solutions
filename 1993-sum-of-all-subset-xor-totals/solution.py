class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        i = [[]]
        k=0
        for x in nums:
            for s in i.copy():
                i.append(s+[x])
        for l in i:
            p=0
            for h in l:
              p^=h
            k+=p
        return k
