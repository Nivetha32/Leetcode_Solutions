class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        c = 0
        
        for i in range(left, right + 1):
            setBits = bin(i).count('1') 
            if self.isPrime(setBits):
                c += 1
        
        return c
    
    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
