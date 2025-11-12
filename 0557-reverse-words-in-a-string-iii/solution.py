class Solution:
    def reverseWords(self, s: str) -> str:
        k= s.split(" ")
        list=[]
        for i in k:
            list.append(i[::-1])
        return " ".join(list)
        
