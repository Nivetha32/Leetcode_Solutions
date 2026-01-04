from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:  

        r= []

        n = len(words)
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    for l in range(n):
                        if l == i or l == j or l == k:
                            continue

                        to = words[i]
                        le = words[j]
                        ri = words[k]
                        bot = words[l]

                        if (
                            to[0] == le[0] and
                            to[3] == ri[0] and
                            bot[0] == le[3] and
                            bot[3] == ri[3]
                        ):
                            r.append([to, le, ri, bot])

        r.sort()
        return r

