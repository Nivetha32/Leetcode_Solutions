class Solution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        int n = nums.size();
        if (2 * k > n) return false;

        for (int i = 0; i <= n - 2 * k; i++) {
            boolean first = true, second = true;

            for (int j = 0; j < k - 1; j++) {
                if (nums.get(i + j) >= nums.get(i + j + 1)) {
                    first = false;
                    break;
                }
            }

            for (int j = 0; j < k - 1; j++) {
                if (nums.get(i + k + j) >= nums.get(i + k + j + 1)) {
                    second = false;
                    break;
                }
            }

            if (first && second) return true;
        }

        return false;
    }
}

