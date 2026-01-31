class Solution:
    def reverseByType(self, s: str) -> str:
        l = []
        sp =[]
        for ch in s:
            if 'a' <= ch<='z':
                l.append(ch)
            else:
                sp.append(ch)

        l.reverse()
        sp.reverse()

        r =[]
        e =0
        li =0

        for ch in s:
            if 'a' <= ch <='z':
                r.append(l[e])
                e+=1
            else:
                r.append(sp[li])
                li+=1
        return "".join(r)
