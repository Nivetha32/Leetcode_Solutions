class Solution {
    public boolean isThree(int n) {
        int r = (int)Math.sqrt(n);
        if(r*r==n && isPrime(r))
        { 
            return true;
        }
        return false;
       }
        public boolean isPrime(int n)
        {
           if(n<2) return false;
           for(int i=2;i<=Math.sqrt(n);i++)
           {
            if(n%i==0) return false;
           }
            
           return true;
        }
}
