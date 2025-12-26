class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sub =[[]]

        for i in nums:
            new =[]
            for k in sub:
                new.append(k+[i])
            sub.extend(new)
        return sub
