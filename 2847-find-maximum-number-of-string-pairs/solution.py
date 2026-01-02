class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        k = set()
        c=0
        for w in words:
          rev = w[::-1]
          if rev in k:
            c+=1
            k.remove(rev)
          else:
            k.add(w)
        return c
        
