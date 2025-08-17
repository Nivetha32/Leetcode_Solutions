class Solution {
    public long maxProfit(int[] prices, int[] strategy, int k) {
        int n=prices.length;
        long[] s=new long[n+1];
        long[] l=new long[n+1];
        
        for(int i=0;i<n;i++)
            {
               s[i+1]=s[i]+(long)strategy[i]*prices[i];
               l[i+1]=l[i]+prices[i];
            }
        long  op= s[n];
        long m=0;
        for(int i=0;i<=n-k;i++)
            {
                int mid = i+k/2;
                int end=i+k;

                long old = s[end]-s[i];
                long newp=l[end]-l[mid];

                long ep=newp-old;
                m=Math.max(m,ep);
            }
        return op+m;
    }
}

