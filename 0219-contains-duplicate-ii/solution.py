class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        n = {}
        for i, num in enumerate(nums):
            if num in n and i - n[num] <= k:
                return True
            n[num] = i
        return False
