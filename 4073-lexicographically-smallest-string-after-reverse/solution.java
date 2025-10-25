class Solution {
    public String lexSmallest(String s) {
        int n = s.length();
        String be = s;
        for(int i=1;i<=n;i++)

            {
                StringBuilder sb = new StringBuilder(s.substring(0,i)).reverse();
                sb.append(s.substring(i));
                String ca = sb.toString();
                if(ca.compareTo(be)<0)
                {
                    be = ca;
                }
                StringBuilder sb1 = new StringBuilder(s.substring(n-i)).reverse();
                String c1 = s.substring(0,n-i)+sb1.toString();
                if(c1.compareTo(be)<0)
                     be =c1;
            }
        return be;
    }
}
