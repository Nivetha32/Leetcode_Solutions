class Solution {
    public int sumDivisibleByK(int[] nums, int k) {
       Map<Integer, Integer> freq = new HashMap<>();
        for (int n : nums) freq.put(n, freq.getOrDefault(n, 0) + 1);

        int sum = 0;
        for (int n : nums)
            if (freq.get(n) % k == 0)
                sum += n;

        return sum;
    }
}
