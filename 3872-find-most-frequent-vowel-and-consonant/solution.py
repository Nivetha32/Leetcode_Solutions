class Solution:
    def maxFreqSum(self, s: str) -> int:
        vow = "aeiou"
        freqO ={}
        freqE={}
        for i in s:
            if i in vow:
                freqE[i]=freqE.get(i,0)+1

            else:
                freqO[i]=freqO.get(i,0)+1
        return max(freqO.values(),default=0)+ max(freqE.values(),default=0)

        
