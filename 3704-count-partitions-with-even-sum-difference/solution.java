class Solution {
    public int countPartitions(int[] nums) {
       
        
        int t = 0;
        for (int y : nums) t+= y;
        
        if ((t & 1) == 0)
            return nums.length - 1;

        
        return 0;
    }
}
