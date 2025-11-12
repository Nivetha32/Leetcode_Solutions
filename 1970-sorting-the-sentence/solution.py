class Solution:
    def sortSentence(self, s: str) -> str:
    #  wor = s.split(' ')
    #  wor.sort(key = lambda x : int(x[-1])
    #  wor

      return " ".join(i[:-1] for i in sorted(s.split(),key=lambda x:x[-1]))
        
