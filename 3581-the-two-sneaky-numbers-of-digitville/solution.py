class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        k=[]
        freq = Counter(nums)
        for key,value in freq.items():
            if value>=2:
                k.append(key)
        return k
       
      

        
