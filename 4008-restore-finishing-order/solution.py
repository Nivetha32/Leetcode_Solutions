class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        f = set(friends)
        r=[]
        for p in order:
            if p in f:
                r.append(p)
        return r
