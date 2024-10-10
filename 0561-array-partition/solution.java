class Solution {
    public int arrayPairSum(int[] n) {
        Arrays.sort(n);
        int sum = 0;
        for (int i = 0; i < n.length; i += 2) {
            sum += n[i];
        }
        return sum;
    }
}

