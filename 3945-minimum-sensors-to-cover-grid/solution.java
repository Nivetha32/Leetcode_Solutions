class Solution {
    public int minSensors(int n, int m, int k) {
        int p=0;
        int s = 2*k+1;
        for(int i=0;i<n;i+=s)
            {
                for(int j=0;j<m;j+=s)
                    {
                        p++;
                    }
            }
      //  int r = (n+s-1)/s;
        //int c= (m+s-1)/s;
        
        return p;
    }
}
