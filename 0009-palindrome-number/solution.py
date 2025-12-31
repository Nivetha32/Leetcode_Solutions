class Solution:
    def isPalindrome(self, x: int) -> bool: 
        k = str(x)
        rev =""
        for i in  k:
            rev = i+rev
        return k == rev

        
