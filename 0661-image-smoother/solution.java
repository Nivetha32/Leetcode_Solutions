class Solution {
    public int[][] imageSmoother(int[][] M) {
        int rows = M.length;
        int cols = M[0].length;
        int[][] result = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                int sum = 0, count = 0;
                for (int ni = i - 1; ni <= i + 1; ni++) {
                    for (int nj = j - 1; nj <= j + 1; nj++) {
                        if (ni >= 0 && ni < rows && nj >= 0 && nj < cols) {
                            sum += M[ni][nj];
                            count++;
                        }
                    }
                }
                result[i][j] = sum / count;
            }
        }

        return result;
    }
}

