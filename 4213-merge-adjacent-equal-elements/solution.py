class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        k = []
        for  y in nums:
            while k and k[-1] == y:
                y+=k.pop()
            k.append(y)
        return k
