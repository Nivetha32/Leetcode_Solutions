class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> seen = new HashSet<>();
        while(n!=1 && !seen.contains(n))
        {
            seen.add(n);
             int s=0;
             while(n>0)
               {
              int k = n%10 ;
              s+=k*k;
              n/=10;
               }
            n=s;
        }
        return n==1;

    }
}
