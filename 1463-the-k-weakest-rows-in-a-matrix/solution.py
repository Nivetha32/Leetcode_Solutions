class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        p = []
        for i in mat:
            c = 0
            for val in i:
                if val == 1:
                    c += 1
            p.append(c)

        n = {}
        for idx, v in enumerate(p):
            n[idx] = v

        g = sorted(n.items(), key=lambda x: x[1])

        r = [i for i, v in g[:k]]
        return r

