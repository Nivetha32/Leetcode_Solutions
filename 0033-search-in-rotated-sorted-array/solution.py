class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k=[]
        for i , key in enumerate(nums):
            if key == target:
                return i
        return -1
