 import java.util.Arrays;
class Solution {
    public int findLHS(int[] nums) {
        Arrays.sort(nums);
        int longest = 0, start = 0;

        for (int end = 0; end < nums.length; end++) {
            while (nums[end] - nums[start] > 1) {
                start++;
            }
            if (nums[end] - nums[start] == 1) {
                longest = Math.max(longest, end - start + 1);
            }
        }

        return longest;
    }
}

