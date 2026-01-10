class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        m = Counter(nums)
        k=[]
        for key , val in m.items():
            if val == 1:
                k.append(key)
        return k
