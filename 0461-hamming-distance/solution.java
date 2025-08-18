class Solution {
    public int hammingDistance(int x, int y) {
        int k = x^y;
        int c=0;
        while(k>0)
        {
           int u= k&1;
           if(u==1)
           {
            c++;
           }
           k>>=1;
        }

       return c; 
    }
}
