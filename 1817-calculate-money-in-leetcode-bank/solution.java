class Solution {
    public int totalMoney(int n) {
        int start = 1;
        int k = start;
        int c = 0;
        for(int i =1;i<=n;i++)
        {
            if(i%7==0)
            {
              c=c+k;
              start++;
              k=start;
            }
            else
            {
                c=c+k;
                k++;
            }
        }
        return c;
    }
}
