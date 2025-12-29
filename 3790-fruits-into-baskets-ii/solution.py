class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c=0
        for i in fruits:
            p = False
            for j in range(len(baskets)):
                if i<=baskets[j]:
                  baskets.pop(j)
                  p = True
                  break
            if not p:
                c+=1
        return c
      

         
