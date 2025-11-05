class Solution {
    public int findNonMinOrMax(int[] nums) {
        if(nums.length<3) return -1;
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        for(int k:nums)
        {
            min = Math.min(min,k);
            max = Math.max(max,k);
        }
        for(int k : nums)
            if(k!=min && k!=max) return k;
        return -1;
    }
}
