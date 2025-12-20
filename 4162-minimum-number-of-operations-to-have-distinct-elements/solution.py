class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s=set()
        k = len(nums)
        for j in range(len(nums)-1,-1,-1):
            if nums[j] in s:
                break
            s.add(nums[j])
            k=j
        return (k+2)//3
        
