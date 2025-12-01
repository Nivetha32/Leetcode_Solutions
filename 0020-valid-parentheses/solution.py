class Solution:
    def isValid(self, s: str) -> bool:
          
        K=[]
        N = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in N.values():
                K.append(c)
            else:
                if not K or K.pop() != N[c]:
                    return False
        return not K
