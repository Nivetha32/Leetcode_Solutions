class Solution:
    def findLucky(self, arr: List[int]) -> int:
        k = Counter(arr)
        l=[]
        for key, value in k.items():
            if value == key:
                l.append(key)
        if len(l)<1:
            return -1
        else:
           return max(l)
              
