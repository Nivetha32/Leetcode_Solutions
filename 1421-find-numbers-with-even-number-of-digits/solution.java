class Solution {
    public int findNumbers(int[] nums){
    int k=0;
        for(int i = 0;i<nums.length;i++)
        {  
            int p = nums[i];
            int c=0;
            while(p!=0)
            {
                int m=p%10;
                c++;
                p/=10;
            }
            if(c%2==0)
            {
                k++;
            }
        }
     return k;
    }
}
     
