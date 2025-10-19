class Solution {
    public int longestBalanced(int[] nums) {
        int n = nums.length;
        int ans = 0;
        int[] ta = nums;

        for (int i = 0; i < n; i++) {
            Map<Integer, Integer> fe = new HashMap<>();
            Map<Integer, Integer> fo = new HashMap<>();
            int de = 0, doo = 0;
            for (int j = i; j < n; j++) {
                int v = ta[j];
                if ((v & 1) == 0) {
                    fe.put(v, fe.getOrDefault(v, 0) + 1);
                    if (fe.get(v) == 1) de++;
                } else {
                    fo.put(v, fo.getOrDefault(v, 0) + 1);
                    if (fo.get(v) == 1) doo++;
                }
                if (de == doo) ans = Math.max(ans, j - i + 1);
            }
        }
        return ans;
    }
}

