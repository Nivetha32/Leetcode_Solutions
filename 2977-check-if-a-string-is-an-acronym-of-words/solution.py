class Solution(object):
    def isAcronym(self, words, s):
        r = "".join(word[0] for word in words)  
        return r == s

