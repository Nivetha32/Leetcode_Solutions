class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        l = set()
        for m in bulbs:
            if m in l:
                l.remove(m)
            else:
                l.add(m)
        return sorted(l)
