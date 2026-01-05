class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        k = Counter(arr)
        s=set()
        for i, val in k.items():
            s.add(val)
        if len(k) == len(s):
            return True
        return False
