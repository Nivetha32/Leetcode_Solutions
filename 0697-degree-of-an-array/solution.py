class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        k = Counter(nums)
        deg = max(k.values())
        fir = {}
        las = {}
        for i , num in enumerate(nums):
                if num not in fir:
                    fir[num]=i
                las[num]=i
        min_l = min(las[key] - fir[key]+1
        for  key, co in k.items()
            if co==deg)
        return min_l


