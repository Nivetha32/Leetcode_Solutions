class Solution {
    public String[] findRelativeRanks(int[] s) {
        int n = s.length;
        int[][] arr = new int[n][2];

        for (int i = 0; i < n; i++) {
            arr[i][0] = s[i];
            arr[i][1] = i;
        }

        Arrays.sort(arr, (a, b) -> Integer.compare(b[0], a[0]));

        String[] r = new String[n];

        for (int i = 0; i < n; i++) {
            if (i == 0) {
                r[arr[i][1]] = "Gold Medal";
            } else if (i == 1) {
                r[arr[i][1]] = "Silver Medal";
            } else if (i == 2) {
                r[arr[i][1]] = "Bronze Medal";
            } else {
                r[arr[i][1]] = String.valueOf(i + 1);
            }
        }

        return r;
    }
}

    
