class Solution:
    def isGood(self, nums: List[int]) -> bool:
        k = max(nums)

        if len(nums)!=k+1:
            return False
        c = Counter(nums)
        if c[k]!=2:
            return False
        for i in range(1,k):
            if c[i]!=1:
                return False
        return True
