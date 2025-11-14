from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      heap = []
      for x,y in Counter(nums).items():
        heap.append((-y,x))
      heapq.heapify(heap)
      re = []
      for i in range(min(k,len(heap))):
        re.append(heapq.heappop(heap)[1])
      return re


      
        
