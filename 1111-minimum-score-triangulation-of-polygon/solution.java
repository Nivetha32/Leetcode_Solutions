class Solution {
    public int minScoreTriangulation(int[] values) {
        int n = values.length;
        int d[][] = new int[n][n];
        for(int row[] : d)
        {
              Arrays.fill(row, -1); 
        }
        return solve(values,0,n-1,d);
    }
    private int solve(int[] values, int i, int j, int[][] dp) {
    if (j - i < 2) return 0;

    if (dp[i][j] != -1) return dp[i][j];

    int minS= Integer.MAX_VALUE;

    for (int k = i + 1; k < j; k++) {
        int sc = values[i] * values[j] * values[k] 
                    + solve(values, i, k, dp) 
                    + solve(values, k, j, dp);
        minS= Math.min(minS, sc);
    }

    dp[i][j] = minS;
    return minS;
}
}

