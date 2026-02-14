class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        k =[]
        for u in words:
            y =0
            for h in u:
                y+=weights[ord(h)-ord('a')]
            j = y%26

            p = chr(ord('z')-j)
            k.append(p)
        return "".join(k)
