class Solution {
    public int maximumSum(int[] arr) {
        int noB = arr[0];
        int oneD = 0;
        int maxS = arr[0];

        for (int i = 1; i < arr.length; i++) {
            int c = arr[i];
            oneD = Math.max(noB, oneD + c);
            noB = Math.max(noB + c, c);
            maxS = Math.max(maxS, Math.max(noB, oneD));
        }

        return maxS;
    }
}

