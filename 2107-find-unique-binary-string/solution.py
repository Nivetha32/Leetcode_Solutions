class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        k=[]
        for i in range(len(nums)):
            if nums[i][i]=='0':
                k.append("1")
            else:
                k.append("0")
        return "".join(k)

