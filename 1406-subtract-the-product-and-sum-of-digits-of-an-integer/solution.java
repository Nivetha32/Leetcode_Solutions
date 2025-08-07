class Solution {
    public int subtractProductAndSum(int n) {
        int s=0;
        int d=1;
        while(n>0)
        {
            int k= n%10;
            s=s+k;
            d=d*k;
            n/=10;
            
        }
        return d-s;
    }
}
