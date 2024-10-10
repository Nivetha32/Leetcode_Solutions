class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxi= 0; 
        int current = 0; 
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                current++; 
                maxi= Math.max(maxi, current); 
            } else {
                current = 0;
            }
        }
 return maxi;
    }
}
 
  
