class Solution:
    def minOperations(self, boxes: str) -> List[int]:
     n = len(boxes)  
     a = [0] * n  
      
  
     b= 0  
     c = 0  
     for i in range(n):  
        a[i] += c  
        if boxes[i] == '1':  
            b+= 1  
        c+= b  
      
     
     b = 0  
     c = 0  
     for i in range(n - 1, -1, -1):  
        a[i] += c  
        if boxes[i] == '1':  
            b += 1  
        c += b  
      
     return a
        
