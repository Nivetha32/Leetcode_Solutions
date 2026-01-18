class Solution {
public int maxCapacity(int[] costs, int[] capacity, int budget) {
int m = costs.length;
int[][] ab = new int[m][2];

for (int i = 0; i < m; i++) {  
        ab[i][0] = costs[i];  
        ab[i][1] = capacity[i];  
    }  

      
    Arrays.sort(ab, (x, y) -> x[0] - y[0]);  

      
    int[] p = new int[m];  
    p[0] = ab[0][1];  
    for (int i = 1; i < m; i++) {  
        p[i] = Math.max(p[i - 1], ab[i][1]);  
    }  

    int an = 0;  

    for (int i = 0; i < m; i++) {  
        if (ab[i][0] >= budget) break;  

          
        an = Math.max(an, ab[i][1]);  

        int rem = budget - ab[i][0] - 1;  

        // Binary search  
        int le = 0, ri = i - 1, id = -1;  
        while (le <= ri) {  
            int mid = (le + ri) / 2;  
            if (ab[mid][0] <= rem) {  
                id = mid;  
                le = mid + 1;  
            } else {  
                ri = mid - 1;  
            }  
        }  

        if (id != -1) {  
            an = Math.max(an, ab[i][1] + p[id]);  
        }  
    }  

    return an;  
}

}
