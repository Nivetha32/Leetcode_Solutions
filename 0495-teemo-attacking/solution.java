class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int total = 0; 
        int n = timeSeries.length; 
        
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                int v = timeSeries[i] - timeSeries[i - 1]; 
                if (v < duration) {
                    total += v; 
                } else {
                    total += duration; 
                }
            } else {
                total += duration; 
            }
        }
        
        return total; 
    }
}

        
