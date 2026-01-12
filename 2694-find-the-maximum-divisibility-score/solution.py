class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        l=[]
        divisors.sort()
        for i in range(0,len(divisors)):
            k=0
            for j in range(0,len(nums)):
                if nums[j]%divisors[i]==0:
                    k+=1
            l.append(k)
        return divisors[l.index(max(l))]

