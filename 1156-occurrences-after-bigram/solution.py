class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        m = text.split()
        r=[]

        for i in range(len(m)-2):
            if m[i] == first and m[i+1]==second:
                r.append(m[i+2])
        return r
