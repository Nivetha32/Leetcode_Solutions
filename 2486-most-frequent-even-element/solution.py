class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
      
        m = Counter(n for n in nums if n%2==0)
        if not m:
            return -1
        mi = max(m.values())
        return min(nu for nu, freq in m.items() if freq == mi)
