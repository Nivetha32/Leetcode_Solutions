class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m=[]
        k = Counter(nums)
        for key, val in k.items():
            if val!=1:
                m.append(key)
        return m[0]

        
