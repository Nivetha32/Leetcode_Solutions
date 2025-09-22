class Solution {
    public int maxFrequencyElements(int[] nums) {
        int[] freq = new int[101];
        for(int n:nums)
        {
            freq[n]++;
        }
        int m=0;
        for(int f:freq)
        {
            if(f>m)  m=f;
        }
        int r=0;
        for(int f:freq)
        {
            if(f==m) r+=f;
        }
        return r;
     
    }
}
