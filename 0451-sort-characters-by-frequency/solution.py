class Solution:
    def frequencySort(self, s: str) -> str:
        he = []
        for x,y in Counter(s).items():
            he.append((-y,x))
        heapq.heapify(he)
        h =""
        while he:
            i = heapq.heappop(he)
            h+=(i[1]*(-i[0]))
        return h
        
