class Solution {
    boolean isP(int n)
    {
        if(n<2) return false;
        for(int i=2;i*i<=n;i++)
            {
                if(n%i==0) return false;
            }
        return true;
    }
    public boolean completePrime(int num) {
        
        String k = String.valueOf(num);
        if(k.length()==1)
        {
            return isP(num);
        }
        for(int i=1;i<=k.length();i++)
            {
                int y = Integer.parseInt(k.substring(0,i));
                if(!isP(y))
                {
                    return false;
                }
            }
        for(int i=0;i<k.length();i++)
            {
                int g = Integer.parseInt(k.substring(i));
                if(!isP(g))
                {
                    return false;
                }
            }
        return true;
        
    }
}
