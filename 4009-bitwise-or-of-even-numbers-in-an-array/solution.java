class Solution {
    public int evenNumberBitwiseORs(int[] nums) {
        int r=0;
        for(int n:nums)
            {
                if(n%2==0)
                {
                    r|=n;
                }
            }
        return r;
    }
}
