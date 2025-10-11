class Solution {
    public int longestSubarray(int[] nums) {
        int[] fibo = nums;
        int max = 2, currlen = 2;
        for(int i=2;i<nums.length;i++)
            {
               if(nums[i] == nums[i-1]+nums[i-2])
               {
                currlen++;
               }
                else
               {
               currlen =2;
               }
        max=Math.max(max,currlen);
            }
    return max;
    }
}
