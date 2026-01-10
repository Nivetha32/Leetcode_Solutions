class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
      k = str(num)[::-1].lstrip('0')
      if k=='':
        m = 0
      else:
        m = int(k[::-1])
      return  m == num
        
