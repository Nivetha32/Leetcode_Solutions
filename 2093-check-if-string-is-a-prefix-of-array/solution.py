class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        h = ""
        for k in words:
            h+=k
            if h==s:
                return True
            if len(h)>len(s):
                return False
        return False
            
           
        
