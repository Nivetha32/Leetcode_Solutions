class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m = []
        for i in image:
            h=[]
            for k in i[::-1]:
                if k==0:
                    h.append(1)
                else:
                    h.append(0)
            m.append(h)
        return m
