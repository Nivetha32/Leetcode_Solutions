class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int s=0;
        int c=0;
        int safe=x;
        while(safe!=0)
        {
            c=safe%10;
            s+=c;
            safe/=10;
        }
        if(x%s == 0)
        {
            return s;
        }
     return -1;
    }
}
