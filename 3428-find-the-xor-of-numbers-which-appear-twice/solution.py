class Solution(object):
    def duplicateNumbersXOR(self, nums):
        seen = set()
        xor_result = 0

        for num in nums:
            if num in seen:  # If it's a duplicate, XOR it
                xor_result ^= num
            else:
                seen.add(num)  # Add to set if seen for the first time

        return xor_result

        
