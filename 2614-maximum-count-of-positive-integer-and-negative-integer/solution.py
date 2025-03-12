class Solution:
    def maximumCount(self, nums):
        neg = sum(1 for x in nums if x < 0)  # Count negative numbers
        pos = sum(1 for x in nums if x > 0)  # Count positive numbers
        return max(neg, pos)  # Return the maximum count

