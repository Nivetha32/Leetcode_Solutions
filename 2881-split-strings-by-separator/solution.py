class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        k=[]
        for i in words:
           k.append(i.split(separator))
        return [i for l  in k for i in l if i!=""]
