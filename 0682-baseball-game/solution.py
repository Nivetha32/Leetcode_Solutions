class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l=[]
        for i in operations:
            if i.lstrip('-').isdigit():
                l.append(int(i))
            elif i == "C":
                l.pop()
            elif i =='D':
                l.append(2*l[-1])
            elif i=='+':
                l.append(l[-1]+l[-2])
             
        return sum(l)
