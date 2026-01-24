class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        m = Counter(words1)
        n = Counter(words2)
        
        return sum(1 for k in m if m[k]==1 and n[k]==1)
          
       
