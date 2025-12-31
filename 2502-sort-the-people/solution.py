class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        k = zip(names,heights)
        p = sorted(k, key = lambda k:k[1], reverse = True)
        return [n[0] for n in p]
