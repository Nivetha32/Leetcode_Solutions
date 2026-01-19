class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        c=0
        ma=0

        for i in range(0,len(gain)):
            c+=gain[i]
            ma = max(ma,c)
        return ma
