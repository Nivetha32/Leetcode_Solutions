class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_d = float('inf')
        
        p=[]
        for i in range(len(arr)-1):
               min_d = min(arr[i+1]-arr[i],min_d)
        for i in range(len(arr)-1):
              if arr[i+1]-arr[i] == min_d:
                p.append([arr[i],arr[i+1]])
        return p

