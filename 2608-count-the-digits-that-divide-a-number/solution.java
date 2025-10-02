class Solution {
    public int countDigits(int num) {
        int n=num;
        int c=0;
        while(n!=0)
        {
            int k = n%10;
            if(num%k==0)
            {
                c++;
            }
            n/=10;
        }
        return c;
    }
}
