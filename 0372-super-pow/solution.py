class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        k = "".join(str(i) for i in b)
        return pow(a,int(k),1337)
