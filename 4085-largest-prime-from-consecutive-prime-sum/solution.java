class Solution {
    boolean isgr(int y)
    {
        if(y<2) return false;
        for(int i=2;i*i<=y;i++)
            {
                if(y%i==0) return false;
            }
        return true;
    }
    int nePy(int l)
    {
        int k = l+1;
        while(!isgr(k)) k++;
        return k;
    }
    public int largestPrime(int n) {
        int v =0;
        int j = 2;
        int hah = 0;
        while(v+j<=n)
            {
                v+=j;
                if(isgr(v))
                 {
                    hah=v;
               }
               j=nePy(j);
            }
        return hah;
    }
}
