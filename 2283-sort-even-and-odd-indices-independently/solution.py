class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        k=[]
        m=[]

        for i in range(len(nums)):
            if i%2!=0:
                k.append(nums[i])
            else:
                m.append(nums[i])
        
        k = sorted(k,reverse = True)
        m = sorted(m)
        od =0
        eve =0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=m[eve]
                eve+=1
            else:
                nums[i]=k[od]
                od+=1
        return nums
