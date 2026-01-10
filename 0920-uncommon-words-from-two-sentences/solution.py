class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
      k = s1.split() + s2.split()
      m = Counter(k)
      l=[]
      for key, val in m.items():
           if val==1:
             l.append(key)
      return l
        



    
