class Solution:
    def minimumK(self, nums: List[int]) -> int:
        p = len(nums)
        e =1
        i=max(max(nums), int(math.sqrt(p))+2)

        def op(l):
            return sum((x+l-1)//l for x in nums)

        n = i

        while e<=i:
            d = (e+i)//2
            if op(d)<= d*d:
                n=d
                i=d-1
            else:
                e=d+1
        return n

        
