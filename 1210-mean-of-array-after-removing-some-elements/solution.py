class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        k = n*5//100
        trim = arr[k:n-k]
        return sum(trim)/len(trim)

