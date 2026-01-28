class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        m = sentence.split(" ")
        for i in range(len(m)):
            if m[i].startswith(searchWord):
               return i+1
        return -1
