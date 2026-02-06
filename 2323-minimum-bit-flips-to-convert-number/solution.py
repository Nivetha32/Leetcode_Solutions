class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        v = start ^ goal
        return bin(v).count('1')
        
