class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        salary.pop(0)
        k=0
        n = len(salary)
        for i in salary:
            k+=i
        return k/n
        
