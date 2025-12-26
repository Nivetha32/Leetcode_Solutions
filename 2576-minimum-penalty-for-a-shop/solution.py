class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        p = customers.count('Y')
        mini = p
        b=0

        for i,j in enumerate(customers):
            if j=='Y':
                p-=1
            else:
                p+=1
            if p<mini:
                mini = p
                b=i+1
        return b
        
