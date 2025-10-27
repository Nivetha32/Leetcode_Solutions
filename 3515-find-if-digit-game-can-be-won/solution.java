class Solution {
    public boolean canAliceWin(int[] nums) {
        int k=0;
        int p=0;
        for(int i=0;i<nums.length;i++)
        {
           if(nums[i]<10)
           {
             k+=nums[i];
           }
           else
           {
            p+=nums[i];
           }
        }
        return k!=p;
        
    }
}
