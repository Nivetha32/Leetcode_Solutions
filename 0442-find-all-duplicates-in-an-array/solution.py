class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        fre = Counter(nums)
        return [key for key,value in fre.items() if value>=2 ]
        
