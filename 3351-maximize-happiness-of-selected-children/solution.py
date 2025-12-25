class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        t= 0
        for j in range(k):
            t += max(happiness[j] - j, 0)
        return t
