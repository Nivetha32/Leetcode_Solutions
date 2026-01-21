class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        m = Counter(word1)
        n = Counter(word2)

        for i in m:
            if abs(m[i]-n.get(i,0))>3:
                return False
        for j in n:
           if j not in m and n[j]>3:
               return False
        return True
