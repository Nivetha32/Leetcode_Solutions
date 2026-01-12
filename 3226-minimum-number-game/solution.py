class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        l=[]
        while nums:
            al = min(nums)
            nums.remove(al)
            bo = min(nums)
            nums.remove(bo)
            l.append(bo)
            l.append(al)
        return l



       
