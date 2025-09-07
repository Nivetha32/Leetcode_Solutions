class Solution {
    public boolean checkPerfectNumber(int num) {
        if(num <= 1) return false;
        int k = 0;
       // boolean b = true;
        for(int i=1;i<=num/2;i++)
        {
            if(num%i==0)
            {
              k+=i;
            }
        }
        return k == num;
    }
}
