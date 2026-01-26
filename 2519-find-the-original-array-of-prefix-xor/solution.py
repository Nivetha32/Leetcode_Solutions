class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        m=[pref[0]]
        for i in range(1,len(pref)):
             m.append(pref[i-1]^pref[i])
        return m
