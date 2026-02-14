class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
            i = defaultdict(int)

            for j in words:
                if len(j)>=k:
                      l = j[:k]
                      i[l]+=1
            h =0
            for d in i.values():
                if d>=2:
                   h+=1
            return h
