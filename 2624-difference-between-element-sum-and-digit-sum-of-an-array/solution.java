class Solution {
    public int differenceOfSum(int[] nums) {
        int s=0, su=0;
        for(int num :nums)
        {
            s+=num;
            while(num!=0)
            {
                int k=num%10;
                su+=k;
                num/=10;
            }
        }
        return Math.abs(s-su);
        
    }
}
