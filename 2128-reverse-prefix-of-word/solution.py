class Solution(object):
    def reversePrefix(self, word, ch):
        index = word.find(ch)
        if index == -1: return word
        
        reversedPart = word[:index] + ch
        return reversedPart[::-1]  + word[index+1:]
