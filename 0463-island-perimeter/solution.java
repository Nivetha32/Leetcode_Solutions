class Solution {
    public int islandPerimeter(int[][] grid) {
        int p = 0; 
        
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == 1) {
                    p += 4; 
                    if (r > 0 && grid[r - 1][c] == 1) p -= 2; 
                    if (c > 0 && grid[r][c - 1] == 1) p -= 2; 
                }
            }
        }
        
        return p; 
    }
}

        

