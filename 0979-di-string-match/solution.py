class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l= 0
        r = len(s)

        rs = []
        for char in s:
            if char == 'I':
                rs.append(l)
                l+=1
            else:
                rs.append(r)
                r-=1
        rs.append(l)
        return rs
