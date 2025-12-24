class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        k = sum(i for i in apple)
        t = sorted(capacity,reverse=True)
        o=0
        c=0
        for i in t:
            o+=i
            c+=1
            if o>=k:
               return c

